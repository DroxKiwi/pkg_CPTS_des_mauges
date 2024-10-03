
# -*- coding: utf-8 -*-

class users(object):
	def __init__(self, pCnx):
		self.oCnx = pCnx
		self.user_id = None
		self.name = None
		self.password = None

	def update(pcpts_o):
		_ocpts = pcpts_o
		_upSQL = ("UPDATE `public`.`cpts` SET "
		"name = " + ("null" if _ocpts.name == None else  ("'" + str(_ocpts.name) + "'")) + ", "
		"password = " + ("null" if _ocpts.password == None else  ("'" + str(_ocpts.password) + "'")) + " "
		"WHERE ID = ID;")
		return _upSQL

	def insert(pcpts_o):
		_ocpts = pcpts_o
		_insSQL = ("INSERT INTO `public`.`cpts` (user_id, name, password) "
		"VALUES ("
		 + ('null' if _ocpts.name == None else "'" + str(_ocpts.name) + "'") + ", "
		 + ('null' if _ocpts.password == None else "'" + str(_ocpts.password) + "')"))
		return _insSQL

	def delete():
		return ""

	def readId(self, pID):
		_sSql = ("SELECT user_id, name, password FROM [public].[cpts] WHERE ID = '" + pID + "'")
		cursor = self.oCnx.cursor(as_dict=True)
		cursor.execute(_sSql)
		row = cursor.fetchone()
		ocpts = cpts(self.oCnx)
		ocpts.user_id = row['user_id']
		ocpts.name = row['name']
		ocpts.password = row['password']
		return ocpts

	def readWhere(self, pWhere):
		_sSql = ("SELECT user_id, name, password FROM [public].[cpts] WHERE " + pWhere )
		cursor = self.oCnx.cursor(as_dict=True)
		cursor.execute(_sSql)
		rows = cursor.fetchall()
		lstcpts = []
		for row in rows:
			ocpts = cpts(self.oCnx)
			ocpts.user_id = row['user_id']
			ocpts.name = row['name']
			ocpts.password = row['password']
			lstcpts.append(ocpts)
		return lstcpts
