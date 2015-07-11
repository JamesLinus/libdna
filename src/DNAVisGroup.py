from pandac.PandaModules import *
from panda3d.core import *
from DNAGroup import DNAGroup
from DNASuitEdge import DNASuitEdge
from DNABattleCell import DNABattleCell

class DNAVisGroup(DNAGroup, DNASuitEdge, DNABattleCell):
	def __init__(self, group, name):
		DNAGroup.__init__(self, name)
		DNASuitEdge.__init__(self, pos=Point3(0, 0, 0))
		DNABattleCell.__init__(self)
		self.visibleGroups = []
		self.visGroup = visGroup
		self.cells = []
	
	def addVisible(self, visGroup):
		self.visGroup = visGroup
		self.visibleGroups.append(visGroup)
	
	def removeVisible(self, visGroup):
		self.visibleGroups.remove(visGroup)
	
	def getNumVisibles(self):
		return len(self.visibleGroups)
	
	def getVisibleName(self, i):
		self.visibleGroups[self.visGroup] = i
		return i
	
	def addSuitEdge(self, edge):
		self.add(edge)
	
	def removeSuitEdge(self, edge):
		self.remove(edge)
	
	def getNumSuitEdges(self):
		return len(self.getEdges())
	
	def getSuitEdge(self):
		return self.getEdges()
	
	def addBattleCell(self, cell):
		self.cells[cell] = cell
	
	def removeBattleCell(self, cell):
		self.cells[cell] = None
	
	def getNumBattleCells(self):
		return len(self.cells)
	
	def getBattleCell(self):
		self.cells[i] = i
		return i
		
