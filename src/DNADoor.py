from pandac.PandaModules import *
from panda3d.core import *
from DNAData import DNAData

class DNADoor(DNAData):
	def __init__(self, node):
		DNAData.__init__(self)
		self.door_code = ''
		self.door_color = VBase4(1, 1, 1, 1)
		self.parent = None

	def setCode(self, door_code):
		self.door_code = door_code

	def getCode(self):
		return self.door_code

	def setColor(self, door_color):
		self.door_color = door_color

	def getColor(self):
		return self.door_color

	def setParent(self, parent):
		self.parent = parent

	def getParent(self):
		return self.parent

	def setupDoor(self, door_node_path, parent, door_origin, store, block, color): #TODO: color = Vec4!
		pass #TODO!
