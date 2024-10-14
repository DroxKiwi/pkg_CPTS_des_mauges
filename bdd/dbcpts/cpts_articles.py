
# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras

class articles(object):
	def __init__(self, pCnx):
		self.oCnx = pCnx
		self.article_id = None
		self.name = None
		self.img = None
		self.tagid = None
		self.actif = None

	def update(particles_o):
		_oarticles = particles_o
		_upSQL = ("UPDATE cpts.public.articles SET "
		"name = " + ("null" if _oarticles.name == None else  ("'" + str(_oarticles.name) + "'")) + ", "
		"img = " + ("null" if _oarticles.img == None else  ("'" + str(_oarticles.img) + "'")) + ", "
		"tag = " + ("null" if _oarticles.tagid == None else  ("'" + str(_oarticles.tagid) + "'")) + ", "
		"actif = " + ("null" if _oarticles.actif == None else  ("'" + str(_oarticles.actif) + "'")) + " "
		"WHERE article_id = " + str(_oarticles.article_id) + ";")
		return _upSQL

	def insert(particles_o):
		_oarticles = particles_o
		_insSQL = ("INSERT INTO cpts.public.articles (name, img, tagid, actif) "
		"VALUES ("
		 + ('null' if _oarticles.name == None else "'" + str(_oarticles.name) + "'") + ", "
		 + ('null' if _oarticles.img == None else "'" + str(_oarticles.img) + "'") + ", "
		 + ('null' if _oarticles.tagid == None else "'" + str(_oarticles.tagid) + "'") + ", "
		 + ('null' if _oarticles.actif == None else "'" + str(_oarticles.actif) + "')"))
		return _insSQL

	def delete(particles_o):
		_oarticles = particles_o
		_insSQL = (f"DELETE FROM cpts.public.articles WHERE article_id = {_oarticles.article_id};")
		return _insSQL

	def readId(self, pID):
		_sSql = ("SELECT article_id, name, img, tagid, actif FROM cpts.public.articles WHERE article_id = '" + str(pID) + "'")
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		row = cursor.fetchone()
		oarticles = articles(self.oCnx)
		oarticles.article_id = row['article_id']
		oarticles.name = row['name']
		oarticles.img = row['img']
		oarticles.tagid = row['tagid']
		oarticles.actif = row['actif']
		return oarticles

	def readWhere(self, pWhere):
		_sSql = ("SELECT article_id, name, img, tagid, actif FROM cpts.public.articles WHERE " + pWhere )
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		rows = cursor.fetchall()
		dict_result = []
		for row in rows:
			dict_result.append(dict(row))
		lstarticles = []
		for row in dict_result:
			oarticles = articles(self.oCnx)
			oarticles.article_id = row['article_id']
			oarticles.name = row['name']
			oarticles.img = row['img']
			oarticles.tagid = row['tagid']
			oarticles.actif = row['actif']
			lstarticles.append(oarticles)
		return lstarticles
