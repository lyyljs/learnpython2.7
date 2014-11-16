import re

rule1 = r'^(\d{3})\-(\d{3,8})$'
test = raw_input('please input a phone number(ex.010-12345): ')

re_phone = re.compile(rule1)

#result = re.match(rule1,test)
result = re_phone.match(test)

if result:
	print 'ok'
else:
	print 'failed'
	raise ValueError('Please input the right number')

print result.group(0)
print result.group(1)
print result.group(2)
print result.groups()
