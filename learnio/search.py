#!/bin/python2
#-*- coding:utf-8 -*-
# author:lyyljs	2014-11-16
# search.py filename [dirname]
# example: search.py test
#	   search.py test /home/abc

import os
import sys

def search(filename,pwd):
	for x in os.listdir(pwd):
		if x[0] != '.':
			temp = os.path.join(pwd,x)
			if os.path.isdir(temp):
				search(filename,temp)
			if os.path.isfile(temp):
				if filename in x:
					print temp


if len(sys.argv) > 3:
	raise SyntaxError('too many arguments')
if len(sys.argv) < 2:
	raise SyntaxError("Please input file's name")

if len(sys.argv)==3:
	if os.path.isdir(sys.argv[2]):
		search(sys.argv[1],sys.argv[2])
	else:
		raise ValueError('%s is not a dir' % sys.argv[2])
else:
	search(sys.argv[1],os.getcwd())

