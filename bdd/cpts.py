
from . dbcpts.cpts_users import users
from . clCnxBdd import cnx

class tusers(users):
	def __init__(self, pDebug=False):
		oCnx = cnx.cpts(pDebug)
		super().__init__(oCnx)
