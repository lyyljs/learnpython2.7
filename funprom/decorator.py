#def log(func):
def log(text = 'call'):
	def decorator(func):
		def wrapper(*args,**kw):
		#print 'call %s():' % func.__name_
			print '%s %s():' % (text,func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator

#@log('execute')
@log()
def now():
	print '2014-11-15'

now()
print now.__name__

#print now()
