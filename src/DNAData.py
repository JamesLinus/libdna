from DNAYaccError import DNAYaccError
from DNAUtil import *
from ply import lex, yacc

class DNAData:
	def __init__(self):
		self.dnaFileName = ''
		self.store = None
		self.data = self

	def setDnaFilename(self, dnaFileName):
		self.dnaFileName = dnaFileName

	def getDnaFilename(self):
		return self.dnaFileName

	def setDnaStorage(self, store):
		self.store = store

	def getDnaStorage(self):
		return self.store

	def getData(self):
		return self.data

	def readDNA(self, file):
		parser = yacc.yacc(debug=0, optimize=0)
		parser.dnaData = self
		parser.parentGroup = parser.dnaData
		parser.dnaStore = self.getDnaStorage()
		parser.nodePath = None
		parser.parse(stream.read())
