
# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras

class globaldata(object):
	def __init__(self, pCnx):
		self.oCnx = pCnx
		self.globaldata_id = None
		self.tel = None
		self.adr = None
		self.postalcode = None
		self.facebook = None
		self.linkedin = None
		self.chiffrepsl = None
		self.chiffrecom = None
		self.chiffrehab = None
		self.hommepageprjstext = None
		self.quisommesnousmaintext = None
		self.mail = None

	def update(pglobaldata_o):
		_oglobaldata = pglobaldata_o
		_upSQL = ("UPDATE cpts.public.globaldata SET "
		"tel = " + ("null" if _oglobaldata.tel == None else  ("'" + str(_oglobaldata.tel) + "'")) + ", "
		"adr = " + ("null" if _oglobaldata.adr == None else  ("'" + str(_oglobaldata.adr) + "'")) + ", "
		"postalcode = " + ("null" if _oglobaldata.postalcode == None else  ("'" + str(_oglobaldata.postalcode) + "'")) + ", "
		"facebook = " + ("null" if _oglobaldata.facebook == None else  ("'" + str(_oglobaldata.facebook) + "'")) + ", "
		"linkedin = " + ("null" if _oglobaldata.linkedin == None else  ("'" + str(_oglobaldata.linkedin) + "'")) + ", "
		"chiffrepsl = " + ("null" if _oglobaldata.chiffrepsl == None else  ("'" + str(_oglobaldata.chiffrepsl) + "'")) + ", "
		"chiffrecom = " + ("null" if _oglobaldata.chiffrecom == None else  ("'" + str(_oglobaldata.chiffrecom) + "'")) + ", "
		"chiffrehab = " + ("null" if _oglobaldata.chiffrehab == None else  ("'" + str(_oglobaldata.chiffrehab) + "'")) + ", "
		"hommepageprjstext = " + ("null" if _oglobaldata.hommepageprjstext == None else  ("'" + str(_oglobaldata.hommepageprjstext) + "'")) + ", "
		"quisommesnousmaintext = " + ("null" if _oglobaldata.quisommesnousmaintext == None else  ("'" + str(_oglobaldata.quisommesnousmaintext) + "'")) + ", "
		"mail = " + ("null" if _oglobaldata.mail == None else  ("'" + str(_oglobaldata.mail) + "'")) + " "
		"WHERE globaldata_id = " + str(_oglobaldata.globaldata_id) + ";")
		return _upSQL

	def insert(pglobaldata_o):
		_oglobaldata = pglobaldata_o
		_insSQL = ("INSERT INTO cpts.public.globaldata (tel, adr, postalcode, facebook, linkedin, chiffrepsl, chiffrecom, chiffrehab, hommepageprjstext, quisommesnousmaintext, mail) "
		"VALUES ("
		 + ('null' if _oglobaldata.tel == None else "'" + str(_oglobaldata.tel) + "'") + ", "
		 + ('null' if _oglobaldata.adr == None else "'" + str(_oglobaldata.adr) + "'") + ", "
		 + ('null' if _oglobaldata.postalcode == None else "'" + str(_oglobaldata.postalcode) + "'") + ", "
		 + ('null' if _oglobaldata.facebook == None else "'" + str(_oglobaldata.facebook) + "'") + ", "
		 + ('null' if _oglobaldata.linkedin == None else "'" + str(_oglobaldata.linkedin) + "'") + ", "
		 + ('null' if _oglobaldata.chiffrepsl == None else "'" + str(_oglobaldata.chiffrepsl) + "'") + ", "
		 + ('null' if _oglobaldata.chiffrecom == None else "'" + str(_oglobaldata.chiffrecom) + "'") + ", "
		 + ('null' if _oglobaldata.chiffrehab == None else "'" + str(_oglobaldata.chiffrehab) + "'") + ", "
		 + ('null' if _oglobaldata.hommepageprjstext == None else "'" + str(_oglobaldata.hommepageprjstext) + "'") + ", "
		 + ('null' if _oglobaldata.quisommesnousmaintext == None else "'" + str(_oglobaldata.quisommesnousmaintext) + "'") + ", "
		 + ('null' if _oglobaldata.mail == None else "'" + str(_oglobaldata.mail) + "')"))
		return _insSQL

	def delete():
		return ""

	def readId(self, pID):
		_sSql = ("SELECT globaldata_id, tel, adr, postalcode, facebook, linkedin, chiffrepsl, chiffrecom, chiffrehab, hommepageprjstext, quisommesnousmaintext, mail FROM cpts.public.globaldata WHERE globaldata_id = '" + pID + "'")
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		row = cursor.fetchone()
		oglobaldata = globaldata(self.oCnx)
		oglobaldata.globaldata_id = row['globaldata_id']
		oglobaldata.tel = row['tel']
		oglobaldata.adr = row['adr']
		oglobaldata.postalcode = row['postalcode']
		oglobaldata.facebook = row['facebook']
		oglobaldata.linkedin = row['linkedin']
		oglobaldata.chiffrepsl = row['chiffrepsl']
		oglobaldata.chiffrecom = row['chiffrecom']
		oglobaldata.chiffrehab = row['chiffrehab']
		oglobaldata.hommepageprjstext = row['hommepageprjstext']
		oglobaldata.quisommesnousmaintext = row['quisommesnousmaintext']
		oglobaldata.mail = row['mail']
		return oglobaldata

	def readWhere(self, pWhere):
		_sSql = ("SELECT globaldata_id, tel, adr, postalcode, facebook, linkedin, chiffrepsl, chiffrecom, chiffrehab, hommepageprjstext, quisommesnousmaintext, mail FROM cpts.public.globaldata WHERE " + pWhere )
		cursor = self.oCnx.cursor(cursor_factory=psycopg2.extras.DictCursor)
		cursor.execute(_sSql)
		rows = cursor.fetchall()
		dict_result = []
		for row in rows:
			dict_result.append(dict(row))
		lstglobaldata = []
		for row in dict_result:
			oglobaldata = globaldata(self.oCnx)
			oglobaldata.globaldata_id = row['globaldata_id']
			oglobaldata.tel = row['tel']
			oglobaldata.adr = row['adr']
			oglobaldata.postalcode = row['postalcode']
			oglobaldata.facebook = row['facebook']
			oglobaldata.linkedin = row['linkedin']
			oglobaldata.chiffrepsl = row['chiffrepsl']
			oglobaldata.chiffrecom = row['chiffrecom']
			oglobaldata.chiffrehab = row['chiffrehab']
			oglobaldata.hommepageprjstext = row['hommepageprjstext']
			oglobaldata.quisommesnousmaintext = row['quisommesnousmaintext']
			oglobaldata.mail = row['mail']
			lstglobaldata.append(oglobaldata)
		return lstglobaldata
