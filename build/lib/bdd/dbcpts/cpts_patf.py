
# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras

class patf(object):
	def __init__(self, pCnx):
		self.oCnx = pCnx
		self.patf_id = None
		self.name = None
		self.subtitle = None
		self.description = None
		self.img = None
		self.tectimeinsert = None
		self.actif = None

	def update(ppatf_o):
		_opatf = ppatf_o
		_upSQL = ("UPDATE cpts.public.patf SET "
		"name = " + ("null" if _opatf.name == None else  ("'" + str(_opatf.name) + "'")) + ", "
		"subtitle = " + ("null" if _opatf.subtitle == None else  ("'" + str(_opatf.subtitle) + "'")) + ", "
		"description = " + ("null" if _opatf.description == None else  ("'" + str(_opatf.description) + "'")) + ", "
		"img = " + ("null" if _opatf.img == None else  ("'" + str(_opatf.img) + "'")) + ", "
		"tectimeinsert = " + ("null" if _opatf.tectimeinsert == None else  ("'" + str(_opatf.tectimeinsert) + "'")) + ", "
		"actif = " + ("null" if _opatf.actif == None else  ("'" + str(_opatf.actif) + "'")) + " "
		"WHERE patf_id = " + str(ppatf_o.patf_id) + ";")
		return _upSQL

	def insert(ppatf_o):
		_opatf = ppatf_o
		_insSQL = ("INSERT INTO cpts.public.patf (name, subtitle, description, img, tectimeinsert, actif) "
		"VALUES ("
		 + ('null' if _opatf.name == None else "'" + str(_opatf.name) + "'") + ", "
		 + ('null' if _opatf.subtitle == None else "'" + str(_opatf.subtitle) + "'") + ", "
		 + ('null' if _opatf.description == None else "'" + str(_opatf.description) + "'") + ", "
		 + ('null' if _opatf.img == None else "'" + str(_opatf.img) + "'") + ", "
		 + ('null' if _opatf.tectimeinsert == None else "'" + str(_opatf.tectimeinsert) + "'") + ", "
		 + ('null' if _opatf.actif == None else "'" + str(_opatf.actif) + "')"))
		return _insSQL

	def delete(ppatf_o):
		_opatf = ppatf_o
		_insSQL = (f"DELETE FROM cpts.public.patf WHERE patf_id = {str(_opatf.patf_id)};")
		return _insSQL

	def readId(self, pID):
		_sSql = ("SELECT patf_id, name, subtitle, description, img, tectimeinsert, actif FROM cpts.public.patf WHERE patf_id = '" + pID + "'")
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		row = cursor.fetchone()
		opatf = patf(self.oCnx)
		opatf.patf_id = row['patf_id']
		opatf.name = row['name']
		opatf.subtitle = row['subtitle']
		opatf.description = row['description']
		opatf.img = row['img']
		opatf.tectimeinsert = row['tectimeinsert']
		opatf.actif = row['actif']
		return opatf

	def readWhere(self, pWhere):
		_sSql = ("SELECT patf_id, name, subtitle, description, img, tectimeinsert, actif FROM cpts.public.patf WHERE " + pWhere )
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		rows = cursor.fetchall()
		dict_result = []
		for row in rows:
			dict_result.append(dict(row))
		lstpatf = []
		for row in dict_result:
			opatf = patf(self.oCnx)
			opatf.patf_id = row['patf_id']
			opatf.name = row['name']
			opatf.subtitle = row['subtitle']
			opatf.description = row['description']
			opatf.img = row['img']
			opatf.tectimeinsert = row['tectimeinsert']
			opatf.actif = row['actif']
			lstpatf.append(opatf)
		return lstpatf
