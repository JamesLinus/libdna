from pandac.PandaModules import *
from panda3d.core import *
from DNASuitPoint import DNASuitPoint

class DNASuitEdge(DNASuitPoint):
	def __init__(self, pos, startPoint=0, endPoint=0, zoneId=''):
		DNASuitPoint.__init__(self, pos)
		self.startPoint = startPoint
		self.endPoint = endPoint
		self.zoneId = zoneId
		self.edges = []
	
	def getStartPoint(self):
		return self.startPoint
	
	def getEndPoint(self):
		return self.endPoint
	
	def setZoneId(self, zoneId):
		self.zoneId = zoneId
	
	def getZoneId(self):
		return self.zoneId
	
	def add(self, edge):
		self.edges.append(edge)
	
	def remove(self, edge):
		self.edges[edge] = None
	
	def getEdges(self):
		return self.edges
