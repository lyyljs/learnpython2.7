#!/bin/python2
# -*- coding:utf-8 -*-

import urllib2,time
from MyDataNode import DataNode

def fetcher(node):
	url = node.url
	try:
		response = urllib2.urlopen(url,timeout=15)
		page = response.read()
		if response.getcode() == 200:
			node.set_html(page)
	except Exception, e:
		raise(e)
	return

if __name__ == '__main__':
	t = DataNode("http://www.sina.com.cn")
	fetcher(t)
	print len(t.html)
	keyword = 'sina'
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(t.html)
	print keyword in soup.get_text()
	#import codecs
	#with codecs.open("sina.html",'w','utf-8') as f:
	#	f.write(t.html)
	#print t.html
