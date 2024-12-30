
# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras

class livret_pages(object):
	def __init__(self, pCnx):
		self.oCnx = pCnx
		self.livret_pages_id = None
		self.numero_page = None
		self.img = None

	def update(plivret_pages_o):
		_olivret_pages = plivret_pages_o
		_upSQL = ("UPDATE cpts.public.livret_pages SET "
		"numero_page = " + ("null" if _olivret_pages.numero_page == None else  ("'" + str(_olivret_pages.numero_page) + "'")) + ", "
		"img = " + ("null" if _olivret_pages.img == None else  ("'" + str(_olivret_pages.img) + "'")) + " "
		"WHERE livret_pages_id = " + str(_olivret_pages.livret_pages_id) + ";")
		return _upSQL

	def insert(plivret_pages_o):
		_olivret_pages = plivret_pages_o
		_insSQL = ("INSERT INTO cpts.public.livret_pages (numero_page, img) "
		"VALUES ("
		 + ('null' if _olivret_pages.numero_page == None else "'" + str(_olivret_pages.numero_page) + "'") + ", "
		 + ('null' if _olivret_pages.img == None else "'" + str(_olivret_pages.img) + "')"))
		return _insSQL

	def delete(plivret_pages_o):
		_olivret_pages = plivret_pages_o
		_insSQL = (f"DELETE FROM cpts.public.livret_pages WHERE livret_pages_id = {str(_olivret_pages.livret_pages_id)};")
		return _insSQL

	def readId(self, pID):
		_sSql = ("SELECT livret_pages_id, numero_page, img FROM cpts.public.livret_pages WHERE livret_pages_id = '" + pID + "'")
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		row = cursor.fetchone()
		olivret_pages = livret_pages(self.oCnx)
		olivret_pages.livret_pages_id = row['livret_pages_id']
		olivret_pages.numero_page = row['numero_page']
		olivret_pages.img = row['img']
		return olivret_pages

	def readWhere(self, pWhere):
		_sSql = ("SELECT livret_pages_id, numero_page, img FROM cpts.public.livret_pages WHERE " + pWhere )
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		rows = cursor.fetchall()
		dict_result = []
		for row in rows:
			dict_result.append(dict(row))
		lstlivret_pages = []
		for row in dict_result:
			olivret_pages = livret_pages(self.oCnx)
			olivret_pages.livret_pages_id = row['livret_pages_id']
			olivret_pages.numero_page = row['numero_page']
			olivret_pages.img = row['img']
			lstlivret_pages.append(olivret_pages)
		return lstlivret_pages
