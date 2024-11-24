
# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras

class pages(object):
	def __init__(self, pCnx):
		self.oCnx = pCnx
		self.pages_id = None
		self.name = None
		self.url = None

	def update(ppages_o):
		return ""

	def insert(ppages_o):
		_opages = ppages_o
		_insSQL = ("INSERT INTO cpts.public.pages (name, url) "
		"VALUES ("
		 + ('null' if _opages.name == None else "'" + str(_opages.name) + "'") + ", "
		 + ('null' if _opages.url == None else "'" + str(_opages.url) + "')"))
		return _insSQL


	def delete():
		return ""

	def readId(self, pID):
		_sSql = ("SELECT pages_id, name, url FROM cpts.public.pages WHERE pages_id = '" + pID + "'")
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		row = cursor.fetchone()
		opages = pages(self.oCnx)
		opages.pages_id = row['pages_id']
		opages.name = row['name']
		opages.url = row['url']
		return opages

	def readWhere(self, pWhere):
		_sSql = ("SELECT pages_id, name, url FROM cpts.public.pages WHERE " + pWhere )
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		rows = cursor.fetchall()
		dict_result = []
		for row in rows:
			dict_result.append(dict(row))
		lstpages = []
		for row in dict_result:
			opages = pages(self.oCnx)
			opages.pages_id = row['pages_id']
			opages.name = row['name']
			opages.url = row['url']
			lstpages.append(opages)
		return lstpages
