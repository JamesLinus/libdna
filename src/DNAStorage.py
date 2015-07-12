from panda3d.core import *

class DNAStorage():
	def __init__(self):
		self.nodes = {}
		self.catalogCodes = {}
		self.fonts = []
		self.textures = []
		self.hoodNodes = {}
		self.placeNodes = {}
		self.visGroups = []
		self.visGroupsAI = []
		self.dnaGroups = []

	def storeNode(self, node, p):
		self.nodes[node] = p

	def storeCatalogCode(self, root, code):
		self.catalogCodes[root] = code

	def storeFont(self, font, dir=None):
		font = font.capitalize()
		if font =='Mickey':
			self.fonts.append(loader.loadFont('phase_3/models/fonts/'+ font + 'Font' + '.bam'))
		elif font == 'Minnie':
			self.fonts.append(loader.loadFont('phase_3/models/fonts/'+ font + 'Font' + '.bam'))
		elif font == 'Suit': #TODO
			pass
		elif font == 'Tt_comedy':
			self.fonts.append(loader.loadFont('phase_3/models/fonts/Comedy.bam'))
		else:
			self.fonts.append(loader.loadFont('phase_3/models/fonts/'+ font + '.bam'))

	def storeTexture(self, name, texture):
		self.textures.append({name: loader.loadTexture(texture)})

	def storeHoodNode(self, node, p):
		self.hoodNodes[node] = p

	def storePlaceNode(self, node, p):
		self.placeNodes[node] = p
	
	def resetDNAVisGroups(self):
		self.visGroups = []

	def getNumDNAVisGroups(self):
		return len(self.visGroups)
	
	def resetDNAVisGroupsAI(self):
		self.visGroupsAI = []
	
	def resetPlaceNodes(self):
		self.placeNodes = {}
	
	def resetDNAGroups(self):
		self.dnaGroups = []

	def resetHood(self):
		self.hoodNodes = {}
		self.placeNodes = {}