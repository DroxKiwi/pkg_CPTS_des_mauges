
# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras

class prod(object):
	def __init__(self, pCnx):
		self.oCnx = pCnx
		self.prod_id = None
		self.prof_ids = None
		self.name = None
		self.img = None
		self.actif = None

	def update(pprod_o):
		_oprod = pprod_o
		_upSQL = ("UPDATE cpts.public.prod SET "
		"prof_ids = " + ("null" if _oprod.prof_ids == None else  ("'" + str(_oprod.prof_ids) + "'")) + ", "
		"name = " + ("null" if _oprod.name == None else  ("'" + str(_oprod.name) + "'")) + ", "
		"img = " + ("null" if _oprod.img == None else  ("'" + str(_oprod.img) + "'")) + ", "
		"actif = " + ("null" if _oprod.actif == None else  ("'" + str(_oprod.actif) + "'")) + " "
		"WHERE prod_id = " + _oprod.prod_id + ";")
		return _upSQL

	def insert(pprod_o):
		_oprod = pprod_o
		_insSQL = ("INSERT INTO cpts.public.prod (prof_ids, name, img, actif) "
		"VALUES ("
		 + ('null' if _oprod.prof_ids == None else "'" + str(_oprod.prof_ids) + "'") + ", "
		 + ('null' if _oprod.name == None else "'" + str(_oprod.name) + "'") + ", "
		 + ('null' if _oprod.img == None else "'" + str(_oprod.img) + "'") + ", "
		 + ('null' if _oprod.actif == None else "'" + str(_oprod.actif) + "')"))
		return _insSQL

	def delete(pprod_o):
		_oprod = pprod_o
		_insSQL = (f"DELETE FROM cpts.public.prod WHERE prod_id = {_oprod.prod_id};")
		return _insSQL

	def readId(self, pID):
		_sSql = ("SELECT prod_id, prof_ids, name, img, actif FROM cpts.public.prod WHERE prod_id = '" + pID + "'")
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		row = cursor.fetchone()
		oprod = prod(self.oCnx)
		oprod.prod_id = row['prod_id']
		oprod.prof_ids = row['prof_ids']
		oprod.name = row['name']
		oprod.img = row['img']
		oprod.actif = row['actif']
		return oprod

	def readWhere(self, pWhere):
		_sSql = ("SELECT prod_id, prof_ids, name, img, actif FROM cpts.public.prod WHERE " + pWhere )
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		rows = cursor.fetchall()
		dict_result = []
		for row in rows:
			dict_result.append(dict(row))
		lstprod = []
		for row in dict_result:
			oprod = prod(self.oCnx)
			oprod.prod_id = row['prod_id']
			oprod.prof_ids = row['prof_ids']
			oprod.name = row['name']
			oprod.img = row['img']
			oprod.actif = row['actif']
			lstprod.append(oprod)
		return lstprod
