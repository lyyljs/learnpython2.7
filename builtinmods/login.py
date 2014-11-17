# -*- coding=utf-8 -*-

import os
import json
import hashlib

def get_md5(h):
	md5 = hashlib.md5(h)
	return md5.hexdigest()

pwd = os.getcwd()
file = os.path.join(pwd,'passwd')

with open(file,'rb') as f:
	try:
		d = json.load(f)
	except ValueError:
		raise ValueError('There is no user!')

user = raw_input('Login: ')
try:
	d[user]
except KeyError:
	raise KeyError('There is no such user named %s!' % user)

passwd = raw_input('Password: ')
salt = 'e10abc394v'
hash = user + passwd + salt

if get_md5(hash) == d[user]:
	print 'login success'
	pass
else:
	print 'login failed'
