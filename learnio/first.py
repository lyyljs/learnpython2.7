#f = open('/home/lyyljs/learnpython2.7/learnio/first.py','r')
with open('/home/lyyljs/learnpython2.7/README.md','r') as f:
	print f.read()
#f.close()

#with open('/home/lyyljs/pic/1.png','rb') as f:
#	print f.read()

with open('/home/lyyljs/learnpython2.7/learnio/test','w') as f:
	f.write('test writefile\n')
