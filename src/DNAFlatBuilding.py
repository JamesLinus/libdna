from pandac.PandaModules import *
from panda3d.core import *
from DNAWall import DNAWall

class DNAFlatBuilding(DNAWall):
	def __init__(self, node=None):
		DNAWall.__init__(self)
		self.width = 0.0

	def setWidth(self, width):
		self.width = width

	def getWidth(self):
		return self.width

	def getCurrentWallHeight(self):
		return 0.0