class Fib(object):
	def __init__(self):
		self.a,self.b = 0,1

	def __iter__(self):
		return self

	def __getitem__(self,n):
		if n < 0:
			raise ValueError('n must >0')
		if isinstance(n,int):
			a,b = 1,1
			for x in range(n):
				a,b = b,a+b
			return a
		if isinstance(n,slice):
			start = n.start
			stop = n.stop
			steps = n.step
			if steps == None:
				steps = 1
			a,b = 1,1
			L = []
			count = 0
			for x in range(stop):
				if x >= start and count % steps == 0:
					L.append(a)
				a,b = b,a+b
				count = count + 1
			return L

	def next(self):
		self.a,self.b = self.b, self.a + self.b
		if self.a >10000:
			raise StopIteration();
		return self.a

f = Fib()
print f[10]
print
print f[5:10]
print
print f[5:10:2]
print
for n in Fib():
	print n
