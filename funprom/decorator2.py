import functools

def log(text = 'call' ):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print '%s %s():' % (text,func.__name__)
			return func(*args,**kw)
		#print 'end call'
		return wrapper
	return decorator

@log()
def f():
	pass
f()
print
print f.__name__
