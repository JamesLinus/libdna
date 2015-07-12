from DNAData import DNAData

def loadDNAFileAI(dnaStore, dnaFile, CSDefault):
	self.dnaData = DNAData()
	self.dnaData.setDnaStorage(dnaStore)
	self.dnaData.setDnaFilename(dnaFile)
	self.dnaData.readDNA(file=open('resources/' + dnaFile, 'r+'))
	return None

def loadDNAFile(dnaStore, dnaFile, CSDefault, value): #TODO: value
	self.dnaData = DNAData()
	self.dnaData.setDnaStorage(dnaStore)
	self.dnaData.setDnaFilename(dnaFile)
	self.dnaData.readDNA(file=open('resources/' + dnaFile, 'r+'))
	return None