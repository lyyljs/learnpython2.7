#-*- coding:utf-8 -*-

import re

name = r'^\<[\w\s]+\>\s+?'
user = r'([0-9a-zA-Z\_\.]+?)'
domain = r'([0-9a-zA-Z\.]{3,20})$'

emailrule = (u'^' + user + u'@' + domain,u'^' + name + user + u'@' + domain)

re_email = []

for x in emailrule:
	re_email.append(re.compile(x))

#re_email = re.compile(emailrule)

bechecked = raw_input('input an email address: ')

while bechecked:
	flag = 1
	for x in re_email:
		result = x.match(bechecked)
		if result:
			print 'ok'
			flag = None
			break
	if flag:
		print 'failed'

#	if re_email.match(bechecked):
#		print 'ok'
#	else:
#		print 'failed'

	bechecked = raw_input('input an email address(or press enter to exit ): ')

