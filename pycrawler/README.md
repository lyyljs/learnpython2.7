spider
==============
spider.py -u url -d deep -f logfile -l loglevel(1-5)  --testself -thread number --dbfile  filepath  --key=”HTML5”
 
参数说明：
-u 指定爬虫开始地址
-d 指定爬虫深度
--thread 指定线程池大小，多线程爬取页面，可选参数，默认10
--dbfile 存放结果数据到指定的数据库（sqlite）文件中
--key 页面内的关键词，获取满足该关键词的网页，可选参数，默认为所有页面
-l 日志记录文件记录详细程度，数字越大记录越详细，可选参数，默认spider.log
--testself 程序自测，可选参数
 
功能描述：
1、指定网站爬取指定深度的页面，将包含指定关键词的页面内容存放到sqlite3数据库文件中
2、程序每隔10秒在屏幕上打印进度信息
3、支持线程池机制，并发爬取网页

参考：
Python教程		http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000
Python爬虫入门教程	http://blog.csdn.net/column/details/why-bug.html
官方文档		https://docs.python.org/
爬虫技术浅析 		http://drops.wooyun.org/tips/3915
sql语言			http://www.w3school.com.cn/sql/sql_quickref.asps
python开发_sqlite3 	http://www.cnblogs.com/hongten/p/hongten_python_sqlite3.html
线程池			http://www.cnblogs.com/nsnow/archive/2010/04/18/1714596.html
Beautiful Soup 4文档	http://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html