from pandac.PandaModules import *
from panda3d.core import *
from DNALandmarkBuilding import DNALandmarkBuilding

class DNACornice(DNALandmarkBuilding):
	node = 'DNACornice'
	
	def __init__(self, node=None):
		DNALandmarkBuilding.__init__(self)
		self.code = ''
		self.cornice_color = VBase4(1, 1, 1, 1)

	def setCode(self, code):
		self.code = code

	def getCode(self):
		return self.code

	def setColor(self, cornice_color):
		self.cornice_color = cornice_color

	def getColor(self):
		return self.cornice_color