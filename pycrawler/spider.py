#coding:utf-8

import Queue, threading, sys
import time, urllib2, re
import logging, argparse
from bs4 import BeautifulSoup

from MyDataNode import DataNode
from Fetcher import fetcher
from Crawler import crawler
from Bloomfilter import bloomfilter
from Sqlite3_fun import sql3_DB


'''
------------------------------------------------------------------------------------------
工作线程
'''
class Worker(threading.Thread):
	worker_count = 0

	def __init__(self, workQueue, timeout=0, **kwds):
		threading.Thread.__init__(self, **kwds)
		self.id = Worker.worker_count
		Worker.worker_count += 1
		self.setDaemon(True)
		self.workQueue = workQueue
		self.timeout = timeout
		logging.info("Start Thread")
		self.start()

	def run(self):
		while 1:
			try:
				callable,args,kwds = self.workQueue.get(timeout=self.timeout)
				res = callable(*args,**kwds)
				logging.info("worker[%2d]: %s" % (self.id, str(res)))
			except Queue.Empty:
				logging.info("Queue is empty")
				break

'''
------------------------------------------------------------------------------------------
线程池
'''

class WorkerManager:
	def __init__(self, num_of_workers=10,timeout=10):
		self.workQueue = Queue.Queue()
		self.workers = []
		self.timeout = timeout
		self._recruitThreads(num_of_workers)

	def _recruitThreads(self,num_of_workers):
		for i in range(num_of_workers):
			worker = Worker(self.workQueue, self.timeout)
			self.workers.append(worker)

	def wait_for_complete(self):
		while len(self.workers):
			worker = self.workers.pop()
			if worker.isAlive():
				worker.join()
			logging.info("End Thread")

	def add_job(self,callable,*args,**kwds):
		self.workQueue.put((callable,args,kwds))

'''
--------------------------------------------------------------------------------------------
爬虫
采用bloomfilter对url进行判重
在网页内容中进行关键字抓取
程序自测测试网络联通以及数据库的链接
'''

class Spider(object):
	def __init__(self, node, depth = 1, num_of_threads = 10, dbfile = 'default.db' , keyword = '', spider_timeout = 100):
		self.node = node
		self.num_of_threads = num_of_threads
		self.depth = depth
		self.spider_timeout = spider_timeout
		self.keyword = keyword
		self.result_pages = []
		self.dbfile = dbfile
		self.state = 1
		self.current = "starting"

		self.total_count = 0
		self.hashtable_size = 10000000
		self.links_hash_table = '0' * self.hashtable_size
		self.ignore_ext = ('js','css','png','jpg','gif','bmp','svg','exif','jpeg','exe','rar','zip','doc','docx','ppt','pptx','pdf','ico')

	def judge_duplication(self, url):
		tmp_list = bloomfilter(url,self.hashtable_size)
		count = 0
		for i in tmp_list:
			if self.links_hash_table[i] == '1':
				count += 1
		if count == 6:
			return True
		else:
			for i in tmp_list:
				self.links_hash_table = self.links_hash_table[:i] + '1' + self.links_hash_table[i+1:]
			return False

	def job(self, node):	
		t = node
		try:
			fetcher(t)
			#print len(t.html)
		except Exception,e:
			logging.warning(e)

		#print "find key start"
		if self.keyword:
			soup = BeautifulSoup(t.html)
			if self.keyword in soup.get_text():
				self.result_pages.append(t)
		else:
			self.result_pages.append(t)
		#print "find key end"

		#print "crawler start"
		try:
			crawler(t)
		except Exception,e:
			logging.warning(e)
		#print "crawler end"

		self.total_count += 1

		if t.depth <= self.depth:
			for i in t.links:
				if i.split('.')[-1] in self.ignore_ext:
					continue
				elif self.judge_duplication(i):
					continue
				else:
					new_node = DataNode(i)
					new_node.set_depth(t.depth + 1)
					self.wm.add_job(self.job,new_node)
		self.current = "fetched:" + str(self.total_count) + "  fetched time: " + str(time.ctime()) + " " + t.url + '\ncurrent depth: ' + str(t.depth)
		#print self.current
		return self.current

	def dbsave(self):
		if self.dbfile != None:
			try:
				self.database = sql3_DB(self.keyword, self.dbfile)
				self.database.SaveDB(self.result_pages)
				self.database.CloseDB()
			except Exception,e:
				logging.warning(e)

	def run(self):
		logging.info('Started')
		self.wm = WorkerManager(self.num_of_threads,self.spider_timeout)
		self.wm.add_job(self.job, self.node)
		self.wm.wait_for_complete()
		self.dbsave()
		logging.info('Finished')

	def testself(self):
		print "Start testing....\n"
		NetConnect = 0
		url_list = ("http://www.sina.com.cn", "http://www.baidu.com", "http://www.sohu.com")
		try:
			for url in url_list:
				response = urllib2.urlopen(url)
				if response.getcode() == 200:
					NetConnect = 1
		except Exception:
			logging.warning(e)
			NetConnect = 0
		if not NetConnect:
			print "Net Connected Error...\n"
		DBerr = 0
		try:
			self.dbsave()
		except:
			logging.warning(e)
			DBerr = 1
		if DBerr:
			print "DataBase Error...\n"
		if not DBerr and NetConnect:
			print "Normal...\n"

'''
---------------------------------------------------------------------------------------------------------
监视线程，每10s打印当前时间，已经爬取页面数量，当前爬取完毕的url和当前爬取深度
'''

class moniter(threading.Thread):
	def __init__(self,Spider):
		threading.Thread.__init__(self)
		self.setDaemon(True)
		self.Spider = Spider
		self.start()

	def run(self):
		while 1:
			if self.Spider:
				time.sleep(10)
				print time.ctime()
				print self.Spider.current

'''
---------------------------------------------------------------------------------------------------------
配置日志文件：1对应CRITICAL，5对应DEBUG，默认等级为3.WARNING
'''

def logconfig(logfile,loglevel):
	Levels = { 1:logging.CRITICAL, 2:logging.ERROR, 3:logging.WARNING, 4:logging.INFO, 5:logging.DEBUG }
	logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(message)s', datefmt = '%m/%d/%Y %I:%M:%S %p',filename = logfile, level = Levels[loglevel])

'''
---------------------------------------------------------------------------------------------------------
参数解析，其中-u 以及-d 是必选参数，其他为可选，默认不创建数据库，存储所有页面，默认线程数为10
'''

if __name__ == '__main__':
	usage_info = '%(prog)s -u url -d deep [-f logfile] [-l loglevel(1-5)] [--testself] [-thread number] [-dbfile filepath] [--key keyworsd]'
	parser = argparse.ArgumentParser(description="This is a spider.", usage=usage_info)
	parser.add_argument('-u',action='store',dest='url',help='starting url')
	parser.add_argument('-d',action='store',dest='deep',type=int,help='dig deep')
	parser.add_argument('-f',action='store',dest='logfile',default='spider.log',help="logfile's name, default=spider.log")
	parser.add_argument('-l',action='store',dest='loglevel',type=int,default=3,help="loglevel(1-5),larger number will get more details. default=3")
	parser.add_argument('--testself',action='store_true',dest='testself',help="test programme")
	parser.add_argument('-thread',action='store',dest='thread_numbers',default=10,type=int,help='the numbers of threads')
	parser.add_argument('-dbfile',action='store',dest='dbfile',help='the name of the database sqlite3')
	parser.add_argument('--key',action='store',dest='keywd',help="page's keyword,and the page will be stored")
	args = parser.parse_args()

	re_url = re.compile('^http:\/\/')
	
	logconfig(args.logfile,args.loglevel)
	if args.testself:
		test_spider = Spider(None)
		test_spider.testself()
	elif not args.url or not args.deep or not re_url.match(args.url):
		parser.print_help()
	else:
		mynode = DataNode(args.url)
		my_spider = Spider(mynode, args.deep, args.thread_numbers, args.dbfile, args.keywd, 200)
		mon = moniter(my_spider)
		my_spider.run()