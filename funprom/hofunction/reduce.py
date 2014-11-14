def add(x,y):
	return x + y
#def str2int(s):
def fn(x,y):
	return x * 10 + y

def char2num(s):
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
#	return reduce(fn,map(char2num,s))

def str2int(s):
	return reduce(fn,map(char2num,s))

print reduce(add, range(1,10,2))
print
print reduce(fn,map(char2num,'13579'))
print
print str2int('12345')
print
