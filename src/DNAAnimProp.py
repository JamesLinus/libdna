from pandac.PandaModules import *
from panda3d.core import *
from DNAProp import DNAProp

class DNAAnimProp(DNAProp):
	def __init__(self):
		DNAProp.__init__(self)
		anim = ''

	def setAnim(self, anim):
		self.anim = anim

	def getAnim(self):
		return self.anim