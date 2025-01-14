
# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras

class orga(object):
	def __init__(self, pCnx):
		self.oCnx = pCnx
		self.orga_id = None
		self.name = None
		self.img = None
		self.role = None
		self.description = None

	def update(porga_o):
		_oorga = porga_o
		_upSQL = ("UPDATE cpts.public.orga SET "
		"name = " + ("null" if _oorga.name == None else  ("'" + str(_oorga.name) + "'")) + ", "
		"img = " + ("null" if _oorga.img == None else  ("'" + str(_oorga.img) + "'")) + ", "
		"role = " + ("null" if _oorga.role == None else  ("'" + str(_oorga.role) + "'")) + ", "
		"description = " + ("null" if _oorga.description == None else  ("'" + str(_oorga.description) + "'")) + " "
		"WHERE orga_id = " + str(_oorga.orga_id) + ";")
		return _upSQL

	def insert(porga_o):
		_oorga = porga_o
		_insSQL = ("INSERT INTO cpts.public.orga (name, img, role, description) "
		"VALUES ("
		 + ('null' if _oorga.name == None else "'" + str(_oorga.name) + "'") + ", "
		 + ('null' if _oorga.img == None else "'" + str(_oorga.img) + "'") + ", "
		 + ('null' if _oorga.role == None else "'" + str(_oorga.role) + "'") + ", "
		 + ('null' if _oorga.description == None else "'" + str(_oorga.description) + "')"))
		return _insSQL

	def delete(porga_o):
		_oorga = porga_o
		_insSQL = (f"DELETE FROM cpts.public.orga WHERE orga_id = {str(_oorga.orga_id)};")
		return _insSQL

	def readId(self, pID):
		_sSql = ("SELECT orga_id, name, img, role, description FROM cpts.public.orga WHERE orga_id = '" + str(pID) + "'")
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		row = cursor.fetchone()
		oorga = orga(self.oCnx)
		oorga.orga_id = row['orga_id']
		oorga.name = row['name']
		oorga.img = row['img']
		oorga.role = row['role']
		oorga.description = row['description']
		return oorga

	def readWhere(self, pWhere):
		_sSql = ("SELECT orga_id, name, img, role, description FROM cpts.public.orga WHERE " + pWhere )
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		rows = cursor.fetchall()
		dict_result = []
		for row in rows:
			dict_result.append(dict(row))
		lstorga = []
		for row in dict_result:
			oorga = orga(self.oCnx)
			oorga.orga_id = row['orga_id']
			oorga.name = row['name']
			oorga.img = row['img']
			oorga.role = row['role']
			oorga.description = row['description']
			lstorga.append(oorga)
		return lstorga
