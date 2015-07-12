from DNAYaccError import DNAYaccError
from ply import lex, yacc
from DNAGroup import DNAGroup
from panda3d.core import *

class DNAData(DNAGroup):
	name = 'DNAData'

	def __init__(self):
		DNAGroup.__init__(self, self.name)
		node = PandaNode('dna')
		self.nodePath = NodePath(node)
		self.Filename = ''
		self.store = None
		self.data = self

	def setDnaFilename(self, Filename):
		self.Filename = Filename

	def getDnaFilename(self):
		return self.dnaFileName

	def setDnaStorage(self, store):
		self.store = store

	def getDnaStorage(self):
		return self.store

	def getData(self):
		return self.data

	def buildGraph(self):
		self.traverse(self.nodePath, self.getDnaStorage())
		if self.nodePath.getChild(0).getNumChildren() == 0:
			return None
		return self.nodePath.getChild(0).getChild(0)

	def readDNA(self, file):
		from DNAUtil import *
		parser = yacc.yacc()
		parser.dnaData = DNAGroup(name='DNAGroup')
		parser.parentGroup = parser.dnaData
		parser.dnaStore = self.getDnaStorage()
		parser.nodePath = None
		parser.parse(file.read())