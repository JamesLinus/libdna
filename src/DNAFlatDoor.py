from pandac.PandaModules import *
from panda3d.core import *
from DNADoor import DNADoor

class DNAFlatDoor(DNADoor):
	node = 'DNAFlatDoor'
	
	def __init__(self, node):
		DNADoor.__init__(self, self.node)
