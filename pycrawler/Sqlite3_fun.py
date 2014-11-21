# coding:utf-8

import sqlite3
from MyDataNode import DataNode

class sql3_DB(object):
	def __init__(self, key, db_file='default.db'):
		self.dbfile = db_file
		self.key = key

		self.conn = sqlite3.connect(self.dbfile)
		self.conn.text_factory = str
		self.cursor = self.conn.cursor()
		self.CreateDB()

	def CreateDB(self):
		try:
			self.cursor.execute("create table data(id INTEGER PRIMARY KEY AUTOINCREMENT,key text,url text,html text)")
			self.conn.commit()
		except:
			pass
			#print "Table data is already exists"

	def SaveDB(self, nodes):
		self.nodes = nodes
		for x in self.nodes:
			self.cursor.execute("insert into data (key,url,html) values (?,?,?)",(self.key, x.url, x.html))
		self.conn.commit()

	def Fetch_url_from_DB(self, keyword = None):
		self.cursor.execute("select * from data")
		r = self.cursor.fetchall()
		result = []
		for i in r:
			if i[1] == self.key:
				result.append(i[2])
		return result

	def CloseDB(self):
		self.cursor.close()
		self.conn.close()

if __name__ == '__main__':
	t = DataNode("http://www.sohu.com")
	from Fetcher import fetcher
	fetcher(t)
	key = 'sina'
	sql_db = sql3_DB('sina')
	sql_db.SaveDB((t,))
	print sql_db.Fetch_url_from_DB()
	sql_db.CloseDB()