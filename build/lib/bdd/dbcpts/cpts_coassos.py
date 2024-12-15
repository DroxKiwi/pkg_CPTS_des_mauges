
# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras

class coassos(object):
	def __init__(self, pCnx):
		self.oCnx = pCnx
		self.coassos_id = None
		self.img = None
		self.redirect_url = None

	def update(pcoassos_o):
		_ocoassos = pcoassos_o
		_upSQL = ("UPDATE cpts.public.coassos SET "
		"img = " + ("null" if _ocoassos.img == None else  ("'" + str(_ocoassos.img) + "'")) + ", "
		"redirect_url = " + ("null" if _ocoassos.redirect_url == None else  ("'" + str(_ocoassos.redirect_url) + "'")) + " "
		"WHERE coassos_id = " + str(_ocoassos.coassos_id) + ";")
		return _upSQL

	def insert(pcoassos_o):
		_ocoassos = pcoassos_o
		_insSQL = ("INSERT INTO cpts.public.coassos (img, redirect_url) "
		"VALUES ("
		 + ('null' if _ocoassos.img == None else "'" + str(_ocoassos.img) + "'") + ", "
		 + ('null' if _ocoassos.redirect_url == None else "'" + str(_ocoassos.redirect_url) + "')"))
		return _insSQL

	def delete():
		return ""

	def readId(self, pID):
		_sSql = ("SELECT coassos_id, img, redirect_url FROM cpts.public.coassos WHERE coassos_id = '" + pID + "'")
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		row = cursor.fetchone()
		ocoassos = coassos(self.oCnx)
		ocoassos.coassos_id = row['coassos_id']
		ocoassos.img = row['img']
		ocoassos.redirect_url = row['redirect_url']
		return ocoassos

	def readWhere(self, pWhere):
		_sSql = ("SELECT coassos_id, img, redirect_url FROM cpts.public.coassos WHERE " + pWhere )
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		rows = cursor.fetchall()
		dict_result = []
		for row in rows:
			dict_result.append(dict(row))
		lstcoassos = []
		for row in dict_result:
			ocoassos = coassos(self.oCnx)
			ocoassos.coassos_id = row['coassos_id']
			ocoassos.img = row['img']
			ocoassos.redirect_url = row['redirect_url']
			lstcoassos.append(ocoassos)
		return lstcoassos
