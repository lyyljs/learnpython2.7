print range(1,11)
print 
print [x * x for x in range(1,11)]
print
print [x * x for x in range(1,11) if x % 2 == 0]
print
print [m + n for m in 'ABC' for n in 'XYZ']
print
d = {'x':'A','y':'B','z':'C'}
print [k + '=' + v for k,v in d.iteritems()]
