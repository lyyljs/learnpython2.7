#!/bin/python2
#-*- coding:utf-8 -*-

class DataNode(object):
	def __init__(self,url):
		self.url = url
		self.html = ''
		self.links = []
		self.depth = 1

	def set_html(self,html):
		self.html = html

	def reset_html(self):
		self.html = ''

	def set_links(self,tmp_list):
		self.links.extend(tmp_list)

	def set_depth(self,depth):
		self.depth += 1
