from pandac.PandaModules import *
from panda3d.core import *
from DNAGroup import DNAGroup

class DNASuitPoint(DNAGroup):
	node = 'DNASuitPoint'

	def __init__(self, index=-1, type=0, pos=Point3(0, 0, 0)):
		DNAGroup.__init__(self, self.node)
		self.index = index
		self.type = type
		self.pos = pos
		self.graphId = 0
		self.lbIndex = 0
	
	def setIndex(self, index):
		self.index = index
	
	def getIndex(self):
		return self.index
	
	def setPointType(self, type):
		self.type = type
	
	def getPointType(self):
		return self.type
	
	def setPos(self, pos):
		self.pos = pos
	
	def getPos(self):
		return self.pos
	
	def setGraphId(self, graphId):
		self.graphId = graphId
	
	def getGraphId(self):
		return self.graphId
	
	def setLandmarkBuildingIndex(self, lbIndex):
		self.lbIndex = lbIndex
	
	def getLandmarkBuildingIndex(self):
		return self.lbIndex
	
	def isTerminal(self): #TODO
		return False
