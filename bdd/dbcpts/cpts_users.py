
# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras

class users(object):
	def __init__(self, pCnx):
		self.oCnx = pCnx
		self.user_id = None
		self.username = None
		self.adminofurl = None
		self.accesstoken = None
		self.bearertoken = None
		self.password = None
		self.actif = None

	def updateToken(pusers_o):
		_ousers = pusers_o
		_upSQL = ("UPDATE cpts.public.users SET "
		"accesstoken = " + ("null " if _ousers.accesstoken == None else  ("'" + str(_ousers.accesstoken) + "' ")) +
		"WHERE user_id = '"+str(_ousers.user_id)+"';")
		print(_upSQL)
		return _upSQL

	def insert(pusers_o):
		return "disabled"

	def delete():
		return ""

	def readId(self, pID):
		_sSql = ("SELECT user_id, username, adminofurl, accesstoken, bearertoken, password, actif FROM cpts.public.users WHERE user_id = '" + str(pID) + "'")
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		row = cursor.fetchone()
		ousers = users(self.oCnx)
		ousers.user_id = row['user_id']
		ousers.username = row['username']
		ousers.adminofurl = row['adminofurl']
		ousers.accesstoken = row['accesstoken']
		ousers.bearertoken = row['bearertoken']
		ousers.password = row['password']
		ousers.actif = row['actif']
		return ousers

	def readWhere(self, pWhere):
		_sSql = ("SELECT user_id, username, adminofurl, accesstoken, bearertoken, password, actif FROM cpts.public.users WHERE " + pWhere )
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		rows = cursor.fetchall()
		dict_result = []
		for row in rows:
			dict_result.append(dict(row))
		lstusers = []
		for row in dict_result:
			ousers = users(self.oCnx)
			ousers.user_id = row['user_id']
			ousers.username = row['username']
			ousers.adminofurl = row['adminofurl']
			ousers.accesstoken = row['accesstoken']
			ousers.bearertoken = row['bearertoken']
			ousers.password = row['password']
			ousers.actif = row['actif']
			lstusers.append(ousers)
		return lstusers
