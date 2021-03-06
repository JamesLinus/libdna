from pandac.PandaModules import *
from panda3d.core import *
from DNAGroup import DNAGroup

class DNAProp(DNAGroup):
	node = 'DNAProp'
	
	def __init__(self, node=None):
		DNAGroup.__init__(self, self.node)
		self.code = ''
		self.color = VBase4(1, 1, 1, 1)
		self.pos = Point3(0, 0, 0)
		self.hpr = Point3(0, 0, 0)
		self.scale = Vec3(0, 0, 0)

	def setPos(self, pos):
		self.pos = pos

	def getPos(self):
		return self.pos

	def setHpr(self, hpr):
		self.hpr = hpr

	def getHpr(self):
		return self.hpr

	def setCode(self, code):
		self.code = code

	def getCode(self):
		return self.code

	def setColor(self, color):
		self.color = color

	def getColor(self):
		return self.color

	def setScale(self, scale):
		self.scale = scale

	def getScale(self):
		return self.scale