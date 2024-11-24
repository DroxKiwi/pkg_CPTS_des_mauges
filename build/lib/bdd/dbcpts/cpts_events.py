
# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras

class events(object):
	def __init__(self, pCnx):
		self.oCnx = pCnx
		self.event_id = None
		self.name = None
		self.subtitle = None
		self.description = None
		self.img = None
		self.tagid = None
		self.startdate = None
		self.enddate = None
		self.tectimeinsert = None
		self.actif = None

	def update(pevents_o):
		_oevents = pevents_o
		_upSQL = ("UPDATE cpts.public.events SET "
		"name = " + ("null" if _oevents.name == None else  ("'" + str(_oevents.name) + "'")) + ", "
		"subtitle = " + ("null" if _oevents.subtitle == None else  ("'" + str(_oevents.subtitle) + "'")) + ", "
		"description = " + ("null" if _oevents.description == None else  ("'" + str(_oevents.description) + "'")) + ", "
		"img = " + ("null" if _oevents.img == None else  ("'" + str(_oevents.img) + "'")) + ", "
		"tagid = " + ("null" if _oevents.tagid == None else  ("'" + str(_oevents.tagid) + "'")) + ", "
		"startdate = " + ("null" if _oevents.startdate == None else  ("'" + str(_oevents.startdate) + "'")) + ", "
		"enddate = " + ("null" if _oevents.enddate == None else  ("'" + str(_oevents.enddate) + "'")) + ", "
		"tectimeinsert = " + ("null" if _oevents.tectimeinsert == None else  ("'" + str(_oevents.tectimeinsert) + "'")) + ", "
		"actif = " + ("null" if _oevents.actif == None else  ("'" + str(_oevents.actif) + "'")) + " "
		"WHERE event_id = " + str(_oevents.event_id) + ";")
		return _upSQL

	def insert(pevents_o):
		_oevents = pevents_o
		_insSQL = ("INSERT INTO cpts.public.events (name, subtitle, description, img, tagid, startdate, enddate, tectimeinsert, actif) "
		"VALUES ("
		 + ('null' if _oevents.name == None else "'" + str(_oevents.name) + "'") + ", "
		 + ('null' if _oevents.subtitle == None else "'" + str(_oevents.subtitle) + "'") + ", "
		 + ('null' if _oevents.description == None else "'" + str(_oevents.description) + "'") + ", "
		 + ('null' if _oevents.img == None else "'" + str(_oevents.img) + "'") + ", "
		 + ('null' if _oevents.tagid == None else "'" + str(_oevents.tagid) + "'") + ", "
		 + ('null' if _oevents.startdate == None else "'" + str(_oevents.startdate) + "'") + ", "
		 + ('null' if _oevents.enddate == None else "'" + str(_oevents.enddate) + "'") + ", "
		 + ('null' if _oevents.tectimeinsert == None else "'" + str(_oevents.tectimeinsert) + "'") + ", "
		 + ('null' if _oevents.actif == None else "'" + str(_oevents.actif) + "')"))
		return _insSQL

	def delete(pevents_o):
		_oevents = pevents_o
		_insSQL = (f"DELETE FROM cpts.public.events WHERE event_id = {_oevents.event_id};")
		return _insSQL

	def readId(self, pID):
		_sSql = ("SELECT event_id, name, subtitle, description, img, tagid, startdate, enddate, tectimeinsert, actif FROM cpts.public.events WHERE event_id = '" + pID + "'")
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		row = cursor.fetchone()
		oevents = events(self.oCnx)
		oevents.event_id = row['event_id']
		oevents.name = row['name']
		oevents.subtitle = row['subtitle']
		oevents.description = row['description']
		oevents.img = row['img']
		oevents.tagid = row['tagid']
		oevents.startdate = row['startdate']
		oevents.enddate = row['enddate']
		oevents.tectimeinsert = row['tectimeinsert']
		oevents.actif = row['actif']
		return oevents

	def readWhere(self, pWhere):
		_sSql = ("SELECT event_id, name, subtitle, description, img, tagid, startdate, enddate, tectimeinsert, actif FROM cpts.public.events WHERE " + pWhere )
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		rows = cursor.fetchall()
		dict_result = []
		for row in rows:
			dict_result.append(dict(row))
		lstevents = []
		for row in dict_result:
			oevents = events(self.oCnx)
			oevents.event_id = row['event_id']
			oevents.name = row['name']
			oevents.subtitle = row['subtitle']
			oevents.description = row['description']
			oevents.img = row['img']
			oevents.tagid = row['tagid']
			oevents.startdate = row['startdate']
			oevents.enddate = row['enddate']
			oevents.tectimeinsert = row['tectimeinsert']
			oevents.actif = row['actif']
			lstevents.append(oevents)
		return lstevents
