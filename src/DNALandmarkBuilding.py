from pandac.PandaModules import *
from panda3d.core import *
from DNAFlatBuilding import DNAFlatBuilding

class DNALandmarkBuilding(DNAFlatBuilding):
	def __init__(self, node=None):
		DNAFlatBuilding.__init__(self)
		self.title = ''
		self.article = ''
		self.code = ''
		self.wall_color = VBase4(1, 1, 1, 1)
		self.building_type = ''

	def setTitle(self, title):
		self.title = title

	def getTitle(self):
		return self.title

	def setArticle(self, article):
		self.article = article

	def getArticle(self):
		return self.article

	def setCode(self, code):
		self.code = code

	def getCode(self):
		return self.code

	def setWallColor(self, wall_color):
		self.wall_color = wall_color

	def getWallColor(self):
		return self.wall_color

	def setBuildingType(self, building_type):
		self.building_type = building_type

	def getBuildingType(self):
		return self.building_type