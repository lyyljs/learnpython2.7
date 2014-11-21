#!/bin/python2
# -*- coding:utf-8 -*-

import re
from bs4 import BeautifulSoup
from MyDataNode import DataNode
from Fetcher import fetcher

def crawler(node):
	html = node.html
	url = node.url
	if url[-1] == '/':
		url = url[:-1]
	link_list = []
	if html == '':
		return
	else:
		try:
			soup = BeautifulSoup(html)
			re_url = re.compile("^http|^/")
			alllinks = soup.find_all("a", href=re_url)
			for i in alllinks:
				if i['href'][0] == '/':
					i['href'] = url + i['href']
				if i['href'][-1] == '/':
					i['href'] = i['href'][:-1]
				link_list.append(i['href'])
			node.set_links(link_list)
		except Exception,e:
			raise(e)
		node.reset_html()
		return

if __name__ == '__main__':
	t = DataNode("http://www.sina.com.cn/")

	fetcher(t)
	print len(t.html)
	crawler(t)
	print len(t.links)
