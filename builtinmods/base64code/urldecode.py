import os
import re
import base64

pwd = os.path.abspath('.')
file = 'urltext'

with open(os.path.join(pwd,file),'rb') as f:
	url = f.read()

while len(url) % 4:
	url = url + '='

print base64.urlsafe_b64decode(url)
