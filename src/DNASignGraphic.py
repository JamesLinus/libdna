from pandac.PandaModules import *
from panda3d.core import *
from DNASignBaseline import DNASignBaseline

class DNASignGraphic(DNASignBaseline):
	def __init__(self, code=''): #TODO
		DNASignBaseline.__init__(self)
		self.code = code
		self.color = VBase4(1, 1, 1, 1)
		self.width = 0.0
		self.height = 0.0

	def setCode(self, code):
		self.code = code

	def getCode(self):
		return self.code

	def setColor(self, color):
		self.color = color

	def getColor(self):
		return self.color

	def setWidth(self, width):
		self.width = width

	def getWidth(self):
		return self.width

	def setHeight(self, height):
		self.height = height

	def getHeight(self):
		return self.height