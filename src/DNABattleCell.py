from pandac.PandaModules import *
from panda3d.core import *
from DNASuitEdge import DNASuitEdge

class DNABattleCell(DNASuitEdge):
	def __init__(self, width=0.0, height=0.0, pos=Point3(0, 0, 0)):
		DNASuitEdge.__init__(self, pos)
		self.width = width
		self.height = height
		self.pos = pos
	
	def setWidthHeight(self, width, height):
		self.width = width
		self.height = height
	
	def getWidth(self):
		return self.width
	
	def getHeight(self):
		return self.height
	
	def setPos(self, pos):
		self.pos = pos
	
	def getPos(self):
		return self.pos
	
	def traverse(self, parent, store): #TODO
		pass
