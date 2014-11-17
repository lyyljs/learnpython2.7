import os
import struct

pwd = os.getcwd()
filename = raw_input('input filename: ')
file = os.path.join(pwd,filename)

with open(file,'rb') as f:
	s = f.read(30)

resolve = struct.unpack('<ccIIIIIIHH',s)
if resolve[0] == 'B' and resolve[1] in ['A','M'] and resolve[3] == 0 and resolve[-2] == 1:
	print "This is a bmp file(size: %d number of colors: %d)." % (resolve[2],resolve[-1])
else:
	print "This file is not bmp."
