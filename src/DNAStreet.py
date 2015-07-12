from pandac.PandaModules import *
from panda3d.core import *
from DNAAnimBuilding import DNAAnimBuilding

class DNAStreet(DNAAnimBuilding): #TODO!
	def __init__(self):
		DNAAnimBuilding.__init__(self)
		self.code = ''
		self.street_texture = ''
		self.sidewalk_texture = ''
		self.curb_texture = ''
		self.street_color = VBase4(1, 1, 1, 1)
		self.sidewalk_color = VBase4(1, 1, 1, 1)
		self.curb_color = VBase4(1, 1, 1, 1)

	def setCode(self, code):
		self.code = code

	def getCode(self):
		return self.code

	def setStreetTexture(self, street_texture):
		self.street_texture = street_texture

	def getStreetTexture(self):
		return self.street_texture

	def setSidewalkTexture(self, sidewalk_texture):
		self.sidewalk_texture = sidewalk_texture

	def getSidewalkTexture(self):
		return self.sidewalk_texture

	def setCurbTexture(self, curb_texture):
		self.curb_texture = curb_texture

	def getCurbTexture(self):
		return self.curb_texture

	def setStreetColor(self, street_color):
		self.street_color = street_color

	def getStreetColor(self):
		return self.street_color

	def setSidewalkColor(self, sidewalk_color):
		self.sidewalk_color = sidewalk_color

	def getSidewalkColor(self):
		return self.sidewalk_color

	def setCurbColor(self, curb_color):
		self.curb_color = curb_color

	def getCurbColor(self):
		return self.curb_color