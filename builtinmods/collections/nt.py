from collections import namedtuple

Point = namedtuple('Point',['x','y'])
Circle = namedtuple('Circle',['x','y','z'])

p = Point(1,2)

print 'p\.x = %d ' % p.x
print 'p\.y = %d ' % p.y
print isinstance(p,Point)
print isinstance(p,tuple)
