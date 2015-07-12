from pandac.PandaModules import *
from panda3d.core import *

class DNAGroup():
	def __init__(self, name):
		self.index = -1
		self.name = name
		self.children = []
		self.parent = NodePath('parent')
	
	def traverse(self, parent, store): #NodePath, DNAStorage
		self.parent = parent
	
	def topLevelTraverse(self, parent, store): #NodePath, DNAStorage
		self.parent = parent
	
	def add(self, child):
		self.children += [child]
	
	def remove(self, child):
		self.children - [child]
	
	def at(self, index):
		return self.children[index]
	
	def current(self):
		return self.index
	
	def getNumChildren(self): #TODO
		return len(self.groups)

	def setParent(self, parentGroup):
		self.parent = parentGroup
	
	def getParent(self):
		return self.parent
	
	def setName(self):
		return self.name  

	def traverse(self, nodePath, dnaStorage):
		node = PandaNode(self.name)
		nodePath = nodePath.attachNewNode(node, 0)
		for child in self.children:
			child.traverse(nodePath, dnaStorage)