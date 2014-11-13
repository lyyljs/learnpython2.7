#!/usr/bin/env python
# -*- coding: utf-8 -*-
print 'ord(\'A\') =',ord('A')
print 'chr(65) =',chr(65)
print 'Then use unicode:'
print u'中文'
a = u'中'
print 'a =',a
t = u'ABC'.encode('utf-8')	#utf to utf-8
t = u'中文'.encode('utf-8')	#utf to utf-8
print 'len(u\'ABC\') =',len(u'ABC')
print 'len(\'ABC\') =',len('ABC')
print 'len(u\'中文\') =',len(u'中文')
print "len('\\xe4\\xb8\\xad\\xe6\\x96\\x87') =",len('\xe4\xb8\xad\xe6\x96\x87')
print "'abc'.decode('utf-8') =",'abc'.decode('utf-8')
