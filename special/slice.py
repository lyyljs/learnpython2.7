tag = '<a> href="http://www.python.org">Python web site</a>'
print tag[9:30]
print tag[32:-4]
print tag[-4:]
print tag[:3]
print tag[:]

# slice http://www.XXX.com
url = raw_input('Please enter the URL: ')
domain = url[11:-4]
print "Domain name: " + domain

number = [1,2,3,4,5]
number[3:3] = [3,3,3]
print number
