names = ['lyy','ljs','floyd']
scores = [95,93,90]
d = {'lyy':95,'ljs':93,'floyd':90}
print d['lyy']
d['adam'] = 85
print d['adam']
print 'ccy' in d
print d.get('ccy')
print d.get('ccy',-1)
print d.pop('adam')
print d
