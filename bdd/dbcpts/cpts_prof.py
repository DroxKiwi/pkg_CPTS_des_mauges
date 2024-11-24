
# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras

class prof(object):
	def __init__(self, pCnx):
		self.oCnx = pCnx
		self.prof_id = None
		self.name = None
		self.subtitle = None
		self.description = None
		self.img = None
		self.tectimeinsert = None
		self.actif = None

	def update(pprof_o):
		_oprof = pprof_o
		_upSQL = ("UPDATE cpts.public.prof SET "
		"name = " + ("null" if _oprof.name == None else  ("'" + str(_oprof.name) + "'")) + ", "
		"subtitle = " + ("null" if _oprof.subtitle == None else  ("'" + str(_oprof.subtitle) + "'")) + ", "
		"description = " + ("null" if _oprof.description == None else  ("'" + str(_oprof.description) + "'")) + ", "
		"img = " + ("null" if _oprof.img == None else  ("'" + str(_oprof.img) + "'")) + ", "
		"tectimeinsert = " + ("null" if _oprof.tectimeinsert == None else  ("'" + str(_oprof.tectimeinsert) + "'")) + ", "
		"actif = " + ("null" if _oprof.actif == None else  ("'" + str(_oprof.actif) + "'")) + " "
		"WHERE prof_id = " + _oprof.prof_id +";")
		return _upSQL

	def insert(pprof_o):
		_oprof = pprof_o
		_insSQL = ("INSERT INTO cpts.public.prof (prof_id, name, subtitle, description, img, tectimeinsert, actif) "
		"VALUES ("
		 + ('null' if _oprof.name == None else "'" + str(_oprof.name) + "'") + ", "
		 + ('null' if _oprof.subtitle == None else "'" + str(_oprof.subtitle) + "'") + ", "
		 + ('null' if _oprof.description == None else "'" + str(_oprof.description) + "'") + ", "
		 + ('null' if _oprof.img == None else "'" + str(_oprof.img) + "'") + ", "
		 + ('null' if _oprof.tectimeinsert == None else "'" + str(_oprof.tectimeinsert) + "'") + ", "
		 + ('null' if _oprof.actif == None else "'" + str(_oprof.actif) + "')"))
		return _insSQL

	def delete():
		return ""

	def readId(self, pID):
		_sSql = ("SELECT prof_id, name, subtitle, description, img, tectimeinsert, actif FROM cpts.public.prof WHERE prof_id = '" + pID + "'")
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		row = cursor.fetchone()
		oprof = prof(self.oCnx)
		oprof.prof_id = row['prof_id']
		oprof.name = row['name']
		oprof.subtitle = row['subtitle']
		oprof.description = row['description']
		oprof.img = row['img']
		oprof.tectimeinsert = row['tectimeinsert']
		oprof.actif = row['actif']
		return oprof

	def readWhere(self, pWhere):
		_sSql = ("SELECT prof_id, name, subtitle, description, img, tectimeinsert, actif FROM cpts.public.prof WHERE " + pWhere )
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		rows = cursor.fetchall()
		dict_result = []
		for row in rows:
			dict_result.append(dict(row))
		lstprof = []
		for row in dict_result:
			oprof = prof(self.oCnx)
			oprof.prof_id = row['prof_id']
			oprof.name = row['name']
			oprof.subtitle = row['subtitle']
			oprof.description = row['description']
			oprof.img = row['img']
			oprof.tectimeinsert = row['tectimeinsert']
			oprof.actif = row['actif']
			lstprof.append(oprof)
		return lstprof
