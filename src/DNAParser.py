from DNAData import DNAData
from DNAStorage import DNAStorage
from DNAUtil import *

def loadDNAFileAI(dnaStore, dnaFile, CSDefault):
	dnaData = DNAData()
	dnaData.setDnaStorage(dnaStore)
	dnaData.setDnaFilename(dnaFile)
	dnaData.readDNA(file=open('resources/' + dnaFile, 'r+'))

def loadDNAFile(dnaStore, dnaFile, CSDefault, value): #TODO: value
	dnaData = DNAData()
	dnaData.setDnaStorage(dnaStore)
	dnaData.setDnaFilename(dnaFile)
	dnaData.readDNA(file=open('resources/' + dnaFile, 'r+'))
	graph = dnaData.buildGraph()
	if not graph is None:
		return graph.getNode(0)
