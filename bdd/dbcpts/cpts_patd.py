
# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras

class patd(object):
	def __init__(self, pCnx):
		self.oCnx = pCnx
		self.patd_id = None
		self.patf_ids = None
		self.name = None
		self.img = None
		self.actif = None

	def update(ppatd_o):
		_opatd = ppatd_o
		_upSQL = ("UPDATE cpts.public.patd SET "
		"patf_ids = " + ("null" if _opatd.patf_ids == None else  ("'" + str(_opatd.patf_ids) + "'")) + ", "
		"name = " + ("null" if _opatd.name == None else  ("'" + str(_opatd.name) + "'")) + ", "
		"img = " + ("null" if _opatd.img == None else  ("'" + str(_opatd.img) + "'")) + ", "
		"actif = " + ("null" if _opatd.actif == None else  ("'" + str(_opatd.actif) + "'")) + " "
		"WHERE patd_id = " + str(ppatd_o.patd_id) + ";")
		return _upSQL

	def insert(ppatd_o):
		_opatd = ppatd_o
		_insSQL = ("INSERT INTO cpts.public.patd (patf_ids, name, img, actif) "
		"VALUES ("
		 + ('null' if _opatd.patf_ids == None else "'" + str(_opatd.patf_ids) + "'") + ", "
		 + ('null' if _opatd.name == None else "'" + str(_opatd.name) + "'") + ", "
		 + ('null' if _opatd.img == None else "'" + str(_opatd.img) + "'") + ", "
		 + ('null' if _opatd.actif == None else "'" + str(_opatd.actif) + "')"))
		return _insSQL

	def delete(ppatd_o):
		_opatd = ppatd_o
		_insSQL = (f"DELETE FROM cpts.public.patd WHERE patd_id = {str(_opatd.patd_id)};")
		return _insSQL

	def readId(self, pID):
		_sSql = ("SELECT patd_id, patf_ids, name, img, actif FROM cpts.public.patd WHERE patd_id = '" + pID + "'")
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		row = cursor.fetchone()
		opatd = patd(self.oCnx)
		opatd.patd_id = row['patd_id']
		opatd.patf_ids = row['patf_ids']
		opatd.name = row['name']
		opatd.img = row['img']
		opatd.actif = row['actif']
		return opatd

	def readWhere(self, pWhere):
		_sSql = ("SELECT patd_id, patf_ids, name, img, actif FROM cpts.public.patd WHERE " + pWhere )
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		rows = cursor.fetchall()
		dict_result = []
		for row in rows:
			dict_result.append(dict(row))
		lstpatd = []
		for row in dict_result:
			opatd = patd(self.oCnx)
			opatd.patd_id = row['patd_id']
			opatd.patf_ids = row['patf_ids']
			opatd.name = row['name']
			opatd.img = row['img']
			opatd.actif = row['actif']
			lstpatd.append(opatd)
		return lstpatd
