from pandac.PandaModules import *
from panda3d.core import *

class DNAGroup():
	def __init__(self, name):
		self.index = -1
		self.name = name
		self.groups = []
		self.parent = NodePath('parent')
	
	def traverse(self, parent, store): #NodePath, DNAStorage
		self.parent = parent
	
	def topLevelTraverse(self, parent, store): #NodePath, DNAStorage
		self.parent = parent
	
	def add(self, group):
		self.groups.append(group)
	
	def remove(self, group):
		self.groups[group] = None
	
	def at(self, index):
		self.index = index
	
	def current(self):
		return self.index
	
	def getNumChildren(self): #TODO
		return len(self.groups)
	
	def getParent(self):
		return self.parent
	
	def setName(self):
		return self.name
