
from . clCnxBdd import cnx
from . dbcpts.cpts_users import users
from . dbcpts.cpts_articles import articles
from . dbcpts.cpts_events import events
from . dbcpts.cpts_tags import tags
from . dbcpts.cpts_pages import pages
from . dbcpts.cpts_prod import prod
from . dbcpts.cpts_prof import prof
from . dbcpts.cpts_patd import patd
from . dbcpts.cpts_patf import patf
from . dbcpts.cpts_coassos import coassos
from . dbcpts.cpts_globaldata import globaldata
from . dbcpts.cpts_livret_pages import livret_pages
from . dbcpts.cpts_orga import orga

class torga(orga):
	def __init__(self, pDebug=False):
		oCnx = cnx.cpts_ps(pDebug)
		super().__init__(oCnx)

class tlivret_pages(livret_pages):
	def __init__(self, pDebug=False):
		oCnx = cnx.cpts_ps(pDebug)
		super().__init__(oCnx)

class tglobaldata(globaldata):
	def __init__(self, pDebug=False):
		oCnx = cnx.cpts_ps(pDebug)
		super().__init__(oCnx)

class tcoassos(coassos):
	def __init__(self, pDebug=False):
		oCnx = cnx.cpts_ps(pDebug)
		super().__init__(oCnx)

class tpatf(patf):
	def __init__(self, pDebug=False):
		oCnx = cnx.cpts_ps(pDebug)
		super().__init__(oCnx)

class tpatd(patd):
	def __init__(self, pDebug=False):
		oCnx = cnx.cpts_ps(pDebug)
		super().__init__(oCnx)

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