from pandac.PandaModules import *
from panda3d.core import *
from DNAStreet import DNAStreet

class DNAWindows(DNAStreet):
	def __init__(self, node=None):
		DNAStreet.__init__(self)
		self.code = ''
		self.count = -1
		self.color = VBase4(1, 1, 1, 1)

	def setCode(self, code):
		self.code = code

	def getCode(self):
		return self.code

	def setWindowCount(self, count):
		self.count = count

	def getWindowCount(self):
		return self.count

	def setColor(self, color):
		self.color = color

	def getColor(self):
		return self.color