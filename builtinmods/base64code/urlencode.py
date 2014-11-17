import base64
import os
import re

result = re.split(r'=+',base64.urlsafe_b64encode(raw_input('input a url: ')))[0]

pwd = os.path.abspath('.')
file = 'urltext'

with open(os.path.join(pwd,file),'wb') as f:
	f.write(result)
