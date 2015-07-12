from pandac.PandaModules import *
from panda3d.core import *
from DNAStorage import DNAStorage

class DNANode(DNAStorage):
	def __init__(self, node): #TODO: node!
		DNAStorage.__init__(self)
		self.pos = VBase3(0, 0, 0)
		self.hpr = VBase3(0, 0, 0)
		self.scale = VBase3(0, 0, 0)
		self.parent = PandaNode(node) #TODO: child_node
		self.nodes = []

	def add(self, parent):
		pass #TODO!

	def remove(self, parent):
		pass #TODO!

	def setPos(self, pos):
		self.pos = pos
	
	def getPos(self):
		return self.pos
	
	def setHpr(self, hpr):
		self.hpr = hpr
	
	def getHpr(self):
		return self.hpr

	def setScale(self, scale):
		self.scale = scale

	def getScale(self):
		return self.scale

	def setParent(self, parent):
		self.parent = parent

	def getParent(self):
		return self.parent