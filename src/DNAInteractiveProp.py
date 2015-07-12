from pandac.PandaModules import *
from panda3d.core import *
from DNAAnimProp import DNAAnimProp

class DNAInteractiveProp(DNAAnimProp):
	def __init__(self):
		DNAAnimProp.__init__(self)
		self.cellId = -1

	def setCellId(self, cellId):
		self.cellId = cellId

	def getCellId(self):
		return self.cellId