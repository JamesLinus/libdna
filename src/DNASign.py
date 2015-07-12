from pandac.PandaModules import *
from panda3d.core import *
from DNAGroup import DNAGroup

class DNASign(DNAGroup):
	def __init__(self, name='DNASign'):
		DNAGroup.__init__(self, name)
		self.code = ''
		self.color = VBase4(1, 1, 1, 1)
		self.scale = Vec3(0, 0, 0) #TODO
		self.pos = Point3(0, 0, 0)
		self.hpr = Point3(0, 0, 0)
	
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

	def setPos(self, pos):
		self.pos = pos
	
	def getPos(self):
		return self.pos
	
	def setHpr(self, hpr):
		self.hpr = hpr
	
	def getHpr(self):
		return self.hpr
