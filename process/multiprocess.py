import os

print 'Process (%s) start...' % os.getpid()
pid = os.fork()
if pid==0:
	print 'Here is child (%s) and parent is %s' % (os.getpid(),os.getppid())
else:
	print 'Here (%s) created a child %s.' % (os.getpid(),pid)
