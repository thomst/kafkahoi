import pygame, vector
from pygame.locals import *
from data import Color, Txt

class Text(pygame.sprite.Sprite, vector.Vector):
	def __init__(self, text, size, vec=0, center=0, underline=0,\
				 color=Color.grew_2, font=Txt.font):
		pygame.sprite.Sprite.__init__(self)
		self.pos = [x/2 for x in self.SCREEN]
		if vec: self.pos = self._vec_add(self.pos, vec)
		self.font = pygame.font.Font(font, size)
		if underline: self.font.set_underline(True)
		self.image = self.font.render(text, True, color)
		self.rect = self.image.get_rect()
		if center == 1: self.rect.center = self.pos
		elif center == 2: self.rect.topright = self.pos
		else: self.rect.topleft = self.pos
