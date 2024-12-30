
# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras

class tags(object):
	def __init__(self, pCnx):
		self.oCnx = pCnx
		self.tag_id = None
		self.name = None
		self.color = None
		self.actif = None

	def update(ptags_o):
		_otags = ptags_o
		_upSQL = ("UPDATE cpts.public.tags SET "
		"name = " + ("null" if _otags.name == None else  ("'" + str(_otags.name) + "'")) + ", "
		"color = " + ("null" if _otags.color == None else  ("'" + str(_otags.color) + "'")) + ", "
		"actif = " + ("null" if _otags.actif == None else  ("'" + str(_otags.actif) + "'")) + " "
		"WHERE tag_id = " + str(_otags.tag_id) + ";")
		return _upSQL

	def insert(ptags_o):
		_otags = ptags_o
		_insSQL = ("INSERT INTO cpts.public.tags (name, color, actif) "
		"VALUES ("
		 + ('null' if _otags.name == None else "'" + str(_otags.name) + "'") + ", "
		 + ('null' if _otags.color == None else "'" + str(_otags.color) + "'") + ", "
		 + ('null' if _otags.actif == None else "'" + str(_otags.actif) + "')"))
		return _insSQL

	def delete(ptags_o):
		_otags = ptags_o
		_insSQL = (f"DELETE FROM cpts.public.tags WHERE tag_id = {str(_otags.tag_id)};")
		return _insSQL

	def readId(self, pID):
		_sSql = ("SELECT tag_id, name, color, actif FROM cpts.public.tags WHERE tag_id = '" + str(pID) + "'")
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		row = cursor.fetchone()
		otags = tags(self.oCnx)
		otags.tag_id = row['tag_id']
		otags.name = row['name']
		otags.color = row['color']
		otags.actif = row['actif']
		return otags

	def readWhere(self, pWhere):
		_sSql = ("SELECT tag_id, name, color, actif FROM cpts.public.tags WHERE " + pWhere )
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		rows = cursor.fetchall()
		dict_result = []
		for row in rows:
			dict_result.append(dict(row))
		lsttags = []
		for row in dict_result:
			otags = tags(self.oCnx)
			otags.tag_id = row['tag_id']
			otags.name = row['name']
			otags.color = row['color']
			otags.actif = row['actif']
			lsttags.append(otags)
		return lsttags
