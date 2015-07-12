from pandac.PandaModules import *
from panda3d.core import *
from DNASignGraphic import DNASignGraphic

class DNASignText(DNASignGraphic):
	def __init__(self):
		DNASignGraphic.__init__(self)
		self.letters = ''

	def setLetters(self, letters):
		self.letters = letters

	def getLetters(self):
		return self.letters