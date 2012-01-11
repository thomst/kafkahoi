import pygame, letter
from pygame.locals import *



class Lives(letter.Letter):
	def __init__(self, image, pos, snd):
		pygame.sprite.Sprite.__init__(self)
		self.image = self.src_img = self.aim_img = pygame.image.load(image)
		self.pos = pos
		self.snd = snd
		self.name = 'live'
		self.rot_dir = 0
		self.sound = 5
		self.rect = self.image.get_rect()
		self.rect.center = self.pos

