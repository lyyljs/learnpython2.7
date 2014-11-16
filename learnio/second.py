import os
print os.name
print os.uname()
#print os.environ
print os.getenv('PATH')
print
pwd = os.path.abspath('.')
print pwd
mydir = os.path.join(pwd,'testdir')
os.mkdir(mydir)
os.rmdir(mydir)
myfile = os.path.join(pwd,'test')
print os.path.split(myfile)
print
print [x for x in os.listdir('.') if os.path.isdir(x)]
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
