import pygame, math, random, vector

class Bug(pygame.sprite.Sprite, vector.Vector):
	def __init__(self, img):
		pygame.sprite.Sprite.__init__(self)
		self.pos = random.sample(range(self.SCREEN[1]), 2)
		self.dir = 0
		self.speed = 0.8
		self.change_dir = 0.0
		self.hit = 0
		self.radius = 40
		self.src_img = pygame.image.load(img)
		self.image = pygame.transform.rotozoom(self.src_img, self.dir, 1)
		self.rect = self.image.get_rect()
		self.rect.center = self.pos

	def update(self, bla, blub):
		if self.hit:
			if pygame.time.get_ticks() - self.time > 4000: self.hit = 0
		else: self._move()
		self.image = pygame.transform.rotozoom(self.src_img, self.dir, 1)
		self.rect = self.image.get_rect()
		self.rect.center = self.pos

	def _move(self):
		if random.randrange(100) < 2:
			self.change_dir = random.choice(range(-3, 3))/2.0
			self.speed = random.choice(range(5, 16))/10.0		
		self._cor_dir()
		self.dir += self.change_dir
		self.plus = self._vec_x_y(self.dir, self.speed)
		self.pos = self._vec_add(self.pos, self.plus)

	def _cor_dir(self):
		vec_mid = self._vec_sub((self.SCREEN[0]/2, self.SCREEN[1]/2), self.pos)
		dir_len = self._vec(vec_mid)
		dir_dif = dir_len[0] - self._vec_angle(self.dir)

		if dir_len[1] > self.SCREEN[1]/2:
			if 0 <= dir_dif < 180 or dir_dif < -180:
				self.change_dir = abs(dir_dif)/100.0
			else: self.change_dir = -abs(dir_dif)/100.0

	def _hit_sets(self):
		self.hit = 1
		self.time = pygame.time.get_ticks()
				
class Legs(pygame.sprite.Sprite, vector.Vector):
	def __init__(self, bug_pos, bug_dir, nr, img, img_vec, img_dir=0):
		pygame.sprite.Sprite.__init__(self)
		self.nr = nr
		self.src_img = pygame.image.load(img)
		self.img_vec = img_vec
		self.img_dir = img_dir

		if self.nr in (1, 2):
			self.v_dir = 29
			self.v_len = 34
			#klein: 26
		elif self.nr in (3, 4):
			self.v_dir = 59
			self.v_len = 30
			#klein: 23
		else:
			self.v_dir = 122
			self.v_len = 30
			#klein: 22
		if self.nr in (2, 4, 6): self.v_dir *= -1

		self.counter_1 = 7
		self.counter_2 = 0
		self.c_ = 14.0
		self.spare = (0, 0)

		self._pos(bug_pos, bug_dir)
		self.step_pos = self.pos_old = self.pos
		self.angle = self._vec_direct(self._vec_sub(self.pos, bug_pos))

	def update(self, bug_pos, bug_dir):
		self._pos(bug_pos, bug_dir)
		self.plus = self._vec_sub(self.pos, self.pos_old)
		self.pos_old = self.pos

		self._counter()
		if self.counter_2 % 2 == 0:
			self._alter([1, 4, 5])
		else:
			self._alter([2, 3, 6])

		self._img(bug_pos)
		self.image = pygame.transform.rotozoom(self.src_img, self.img_rot, 1)
		self.rect = self.image.get_rect()
		self.rect.center = self.img_pos

	def _pos(self, bug_pos, bug_dir):
		vec_pos = self._vec_x_y(bug_dir + self.v_dir, self.v_len)
		self.pos  = self._vec_add(bug_pos, vec_pos)

	def _alter(self, group):
		if self.nr in group:
			plus = self._vec_add(self.plus, self._vec_multi(self.spare, 1.0/self.c_))
			self.step_pos = self._vec_add(self.step_pos, plus)
		else: 
			self.spare = self._vec_add(self.spare, self.plus)

	def _counter(self):
		self.counter_1 += 1
		if self.counter_1 % self.c_ == 0:
			self.counter_2 += 1
			if self.counter_2 % 2 == 0 and self.nr in [2, 3, 6]: self.spare = (0, 0)
			elif self.counter_2 % 2 == 1 and self.nr in [1, 4, 5]: self.spare = (0, 0)

	def _img(self, bug_pos):
		angle = self._vec_direct(self._vec_sub(self.step_pos, bug_pos))
		self.img_rot = self.img_dir + angle - self.angle

		dir_len = self._vec(self.img_vec)
		img_cor = self._vec_x_y(dir_len[0] + self.img_rot, dir_len[1])
		self.img_pos = self._vec_sub(self.step_pos, img_cor)

class Feeler(pygame.sprite.Sprite, vector.Vector):
	def __init__(self, nr, img, img_vec):
		pygame.sprite.Sprite.__init__(self)
		self.src_img = pygame.image.load(img)
		self.nr = nr
		self.dir_len = self._vec(img_vec)
		self.change = 0
		self.ch_ = 2.5

		if nr == 1:
			self.v_dir = 14
			self.v_len = 31
			#klein: 24
		else:
			self.v_dir = 353
			self.v_len = 31

	def update(self, bug_pos, bug_dir):
		vec_pos = self._vec_x_y(self.v_dir + bug_dir, self.v_len)
		self.pos = self._vec_add(bug_pos, vec_pos)

		self._rot(bug_dir)

		self.img_vec = self._vec_x_y(self.dir_len[0] + self.rot, self.dir_len[1])
		self.img_pos = self._vec_sub(self.pos, self.img_vec)

		self.image = pygame.transform.rotozoom(self.src_img, self.rot, 1)
		self.rect = self.image.get_rect()
		self.rect.center = self.img_pos

	def _rot(self, bug_dir):
		if self.nr == 1 and not 5 > self.change > -45: self.ch_ *= -1
		elif self.nr == 2 and not -15 < self.change < 35: self.ch_ *= -1
		elif random.randrange(20) < 1: self.ch_ *= -1

		self.change += self.ch_
		self.rot = bug_dir + self.change



