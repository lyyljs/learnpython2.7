import logging

try:
	print 'try...'
	r = 10 / int('a')
	print 'result:', r
#except ValueError,e:
#	print 'ValueError:',e
except ZeroDivisionError,e:
	print 'ZeroDivisionErrpr:',e
else:
	print 'no error!'
finally:
	print 'finally..'
print 'End'
