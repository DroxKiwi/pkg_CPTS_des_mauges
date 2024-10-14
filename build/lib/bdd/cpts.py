
from . clCnxBdd import cnx
from . dbcpts.cpts_users import users
from . dbcpts.cpts_articles import articles
from . dbcpts.cpts_tags import tags

class tusers(users):
	def __init__(self, pDebug=False):
		oCnx = cnx.cpts_ps(pDebug)
		super().__init__(oCnx)

class tarticles(articles):
	def __init__(self, pDebug=False):
		oCnx = cnx.cpts_ps(pDebug)
		super().__init__(oCnx)

class ttags(tags):
	def __init__(self, pDebug=False):
		oCnx = cnx.cpts_ps(pDebug)
		super().__init__(oCnx)