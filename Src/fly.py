import math, random, vector
import pygame


class Fly(pygame.sprite.Sprite, vector.Vector):
	def __init__(self, speed, cor_list, img_list):
		pygame.sprite.Sprite.__init__(self)
		self._pos()
		self.speed = speed
		self.cor_list = cor_list
		self._img_list(img_list)
		self.dir = random.randrange(360)
		self.randm = random.choice(range(-4, 4))
		self.radius = 20
		self.i = self.c = 0

	def _pos(self):
		xy = [random.choice((-10, self.SCREEN[0]+10))]
		xy.append(random.randrange(self.SCREEN[1]))
		self.pos = xy.pop(random.choice((0, 1))), xy[0]

	def _img_list(self, img):
		self.img_list = []
		for i in img:
			self.img_list.append(pygame.image.load(i))

	def update(self, done=0):
		self._direct()
		self._cor(done)
		self._img()
		self._osszil()

		self.pos = self._vec_add(self.pos, self.plus)
		self.rect.center = self.pos

	def _direct(self):
		self.dir += self.randm
		if random.randrange(100) < 2: self.randm = random.choice(range(-6, 6))
		self.plus = self._vec_x_y(self.dir, self.speed)

	def _cor(self, done):
		if not done: vec_cor = self._vec_cor(self.pos, *self.cor_list)
		else: vec_cor = self._vec_done(self.pos)
		self.plus = self._vec_add(self.plus, vec_cor)

	def _img(self):
		self.img = self.img_list[self.c % 2]
		self.c += 1
		self.rot_dir = self._vec_direct(self.plus)
		self.image = pygame.transform.rotozoom(self.img, self.rot_dir, 1)
		self.rect = self.image.get_rect()

	def _osszil(self):
		self.dir_oss = self.dir -90
		if self.i < 360: 
			self.speed_oss = math.cos(math.radians(self.i)) * 2
			self.i += 20
		else: self.i = 0
		oss = self._vec_x_y(self.dir_oss, self.speed_oss)
		self.plus = self._vec_add(self.plus, oss)



