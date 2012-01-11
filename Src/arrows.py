import math, random, vector
import pygame

class Arrow(pygame.sprite.Sprite, vector.Vector):
	def __init__(self, image, direct, star_pos):
		pygame.sprite.Sprite.__init__(self)
		self.dir = direct
		self.star_pos = star_pos
		self.src_image = pygame.image.load(image)
		self.image = pygame.transform.rotozoom(self.src_image, self.dir, 1)
		self.rect = self.image.get_rect()
		self.pos = self.star_pos[0], self.star_pos[1]

	def update(self):
		vec = self._vec_x_y(self.dir, 15)
		self.pos = [self.pos[i] + vec[i] for i in (0, 1)]
		self.rect.center = self.pos

