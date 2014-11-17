#-*- coding=utf-8 -*-

import os
import json
import hashlib

def get_md5(h):
	md5 = hashlib.md5(h)
	return md5.hexdigest()

pwd = os.getcwd()
filename = 'passwd'
file = os.path.join(pwd,filename)
with open(file,'rb') as f:
	try:
		d = json.load(f)
	except ValueError:
		d = {}
	finally:
		f.close()

user = raw_input('user: ')
passwd = raw_input('passwd: ')
salt = 'e10abc394v'
hash = user + passwd + salt
d[user] = get_md5(hash)

result = json.dumps(d)

with open(file,'wb') as f:
	f.write(result)
