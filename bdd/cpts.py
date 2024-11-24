
from . clCnxBdd import cnx
from . dbcpts.cpts_users import users
from . dbcpts.cpts_articles import articles
from . dbcpts.cpts_events import events
from . dbcpts.cpts_tags import tags
from . dbcpts.cpts_pages import pages
from . dbcpts.cpts_prod import prod
from . dbcpts.cpts_prof import prof

class tprod(prod):
	def __init__(self, pDebug=False):
		oCnx = cnx.cpts_ps(pDebug)
		super().__init__(oCnx)

class tprof(prof):
	def __init__(self, pDebug=False):
		oCnx = cnx.cpts_ps(pDebug)
		super().__init__(oCnx)

class tusers(users):
	def __init__(self, pDebug=False):
		oCnx = cnx.cpts_ps(pDebug)
		super().__init__(oCnx)

class tarticles(articles):
	def __init__(self, pDebug=False):
		oCnx = cnx.cpts_ps(pDebug)
		super().__init__(oCnx)

class tevents(events):
	def __init__(self, pDebug=False):
		oCnx = cnx.cpts_ps(pDebug)
		super().__init__(oCnx)

class ttags(tags):
	def __init__(self, pDebug=False):
		oCnx = cnx.cpts_ps(pDebug)
		super().__init__(oCnx)

class tpages(pages):
	def __init__(self, pDebug=False):
		oCnx = cnx.cpts_ps(pDebug)
		super().__init__(oCnx)