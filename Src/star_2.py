import math, random, vector
import pygame

class Star(pygame.sprite.Sprite, vector.Vector):
	def __init__(self, mouse_pos, image, change_dir, speed_quot, cor_list, control=0):
		pygame.sprite.Sprite.__init__(self)
		self.src_image = pygame.image.load(image)
		self.change_dir = change_dir
		self.speed_quotient = speed_quot
		self.cor_list = cor_list
		self.pos = mouse_pos
		self.control = control
		self.right = self.left = 0
		self.radius = 30
		self.rot_dir = self.plus_rot= 0
		self.crash = self.dir = 0

	def update(self, mouse_pos, done=0):
		self._move(mouse_pos)
		if not done: vec_cor = self._vec_cor(self.pos, *self.cor_list)
		else: vec_cor = self._vec_done(self.pos)
		self.plus = self._vec_add(self.plus, vec_cor)

		if self.control: self._rotate_control()
		if self.crash: self._crash()
		elif not self.control: self.rot_dir = self._vec_direct(self.plus)

		self.pos = self._vec_add(self.pos, self.plus)
		self.image = pygame.transform.rotozoom(self.src_image, self.rot_dir, 1)
		self.rect = self.image.get_rect()
		self.rect.center = self.pos

	def _move(self, mouse_position):
		"""regulaere Bewegung in Abhaengigkeit zur Mausposition"""
		m_x, m_y = mouse_position
		x, y = self.pos
		self.dir += self.change_dir
		rad = self.dir * math.pi / 180

		self.plus = [math.sin(rad) * ((m_x - x)/self.speed_quotient)]
		self.plus.append(math.cos(rad) * ((m_y - y)/self.speed_quotient))

##### kontrollierte Rotation #####
	def _rotate_control(self):
		if self.left + self.right != 0:
			if self.right and self.plus_rot< 30: self.plus_rot+= 1.5
			if self.left and self.plus_rot> -30: self.plus_rot-= 1.5
			self.rot_dir += self.plus_rot
		elif abs(self.plus_rot) > 1: 
			self.plus_rot*= 0.82
			self.rot_dir += self.plus_rot

##### Bei einem Crash #####
	def _crash(self):
		self._timer()
		self._reject()
		self._rotate_reject()

	def _crash_sets(self, bads_pos):
		self.crash = 1
		self.bads_pos = bads_pos
		self.reject = 25
		self.plus_rej_rot = random.choice((-35, 35))
		self.time = pygame.time.get_ticks()

	def _timer(self):
		if pygame.time.get_ticks() - self.time > 2800:
			self.crash = 0

	def _reject(self):
		vec_rej = self._vec_sub(self.pos, self.bads_pos)
		rej_dir = self._vec_direct(vec_rej)

		if self.reject > 1:self.reject *= 0.96
		else: self.reject = 0

		plus = self._vec_x_y(rej_dir, self.reject)
		self.plus = self._vec_add(self.plus, plus)

	def _rotate_reject(self):
		self.plus_rej_rot *= 0.98
		self.rot_dir += self.plus_rej_rot


##################################################

	def _move_out(self):
		if abs(self.plus_x * self.plus_y) > 0.001:
			self.plus_x *= 0.8
			self.plus_y *= 0.8

			self.x += self.plus_x
			self.y += self.plus_y
			self.pos = self.x, self.y
			

