from pandac.PandaModules import *
from panda3d.core import *
from DNASign import DNASign

class DNASignBaseline(DNASign):
	def __init__(self):
		DNASign.__init__(self)
		self.code = ''
		self.color = VBase4(1, 1, 1, 1)
		self.font = None
		self.indent = 0.0
		self.kern = 0.0
		self.wiggle = 0.0
		self.stumble = 0.0
		self.stomp = 0.0
		self.width = 0.0
		self.height = 0.0
		self.flags = ''
		self.pos = Vec3(0, 0, 0)
		self.hpr = Vec3(0, 0, 0)
		self.size = Vec3(0, 0, 0)
	
	def setCode(self, code):
		self.code = code
	
	def getCode(self):
		return self.code
	
	def setColor(self, color):
		self.color = color
	
	def getColor(self):
		return self.color
	
	def setFont(self, font):
		self.font = font
	
	def getFont(self):
		if font == None:
			return None
		return self.font
	
	def setIndent(self, indent):
		self.indent = indent
	
	def getIndent(self):
		return self.indent
	
	def setKern(self, kern):
		self.kern = kern
	
	def getKern(self):
		return self.kern
	
	def getCurrentKern(self):
		return 0.0
	
	def setWiggle(self, wiggle):
		self.wiggle = wiggle
	
	def getWiggle(self):
		return self.wiggle
	
	def getCurrentWiggle(self):
		return 0.0
	
	def setStumble(self, stumble):
		self.stumble = stumble
		
	def getStumble(self):
		return self.stumble
	
	def getCurrentStumble(self):
		return 0.0
	
	def setStomp(self, stomp):
		self.stomp = stomp
	
	def getStomp(self):
		return self.stomp
	
	def getCurrentStomp(self):
		return 0.0
	
	def setWidth(self, width):
		self.width = width
	
	def getWidth(self):
		return self.width
	
	def setHeight(self, height):
		self.height = height
	
	def getHeight(self):
		return self.height
	
	def setFlags(self, flags):
		self.flags = flags
	
	def getFlags(self):
		return self.flags
	
	def isFirstLetterOfWord(self, letter):
		if letter.capitalize(): #TODO
			return True
		else:
			return False
	
	def resetCounter(self):
		pass
	
	def incCounter(self):
		pass
	
	def setPos(self, pos):
		self.pos = pos
	
	def getPos(self):
		return self.pos
	
	def setHpr(self, hpr):
		self.hpr = hpr
	
	def getHpr(self):
		return self.hpr
	
	def setSize(self, size):
		self.size = size
	
	def getSize(self):
		return self.size
	
	def baselineNextPosHprScale(self, pos, hpr, scale, size):
		self.setPos(pos)
		self.setHpr(hpr)
		self.setScale(scale)
		self.setSize(size)
