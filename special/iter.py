d = {'a':1,'b':2,'c':3}
for key in d:
	print key
for value in d.itervalues():
	print value
print
for k,v in d.iteritems():
	print k,v
print
from collections import Iterable
print isinstance('abc',Iterable)
print isinstance(123,Iterable)
print

for i,value in enumerate(['A','B','C']):
	print i,value
