from pandac.PandaModules import *
from panda3d.core import *
from DNANode import DNANode

class DNAWall(DNANode):
	node = 'wall'
	
	def __init__(self, node=None):
		DNANode.__init__(self, self.node)
		self.code = ''
		self.height = 0.0
		self.color = VBase4(1, 1, 1, 1)

	def setCode(self, code):
		self.code = code

	def getCode(self):
		return self.code

	def setHeight(self, height):
		self.height = height

	def getHeight(self):
		return self.height

	def setColor(self, color):
		self.color = color

	def getColor(self):
		return self.color