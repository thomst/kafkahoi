import pygame, math, random, vector
from pygame.locals import *
from data import Txt, Color



class Letter(pygame.sprite.Sprite, vector.Vector, Txt, Color):
	def __init__(self, name, snd):
		pygame.sprite.Sprite.__init__(self)
		self.snd = snd
		self.name = name
		self.radius = 20
		self.fnt = pygame.font.Font(self.font, self.sz_poem)
		self.image = self.src_img = self.fnt.render(name, True, self.colors[0])
		self.poem_img = self.fnt.render(self.name, True, self.colors[1])
		self.pos =	random.choice(self.L_SCREEN),\
					random.choice(self.L_SCREEN)
		self.rot_dir = random.randrange(360)
		self.image = pygame.transform.rotozoom(self.src_img, self.rot_dir, 1)
		self.rect = self.image.get_rect()
		self.rect.center = self.pos
		self.aim_pos = self.rot_dir = self.aim = 0
		self.sound = 4

	def update(self, mov_list=0):
		if mov_list: self._move(mov_list)
		if self.aim_pos: self._aim_pos()
		self.rect = self.image.get_rect()
		if self.aim: self.rect.bottomleft = self.pos
		else: self.rect.center = self.pos

	def _move(self, mov_list):
		if len(mov_list) <= self.nr * 5: self.pos = mov_list[-1]
		else: self.pos = mov_list[self.nr * 5]
		
	def _nr(self, nr):
		self.nr = nr

	def _crash_sets(self, aim=0, pos=0):
		self.aim = aim != 0
		if pos: self.pos = pos
		self.crash_dir = random.randrange(360)
		self.change_dir = random.choice([-4, 4])
		self.crash_len = 18
		self.aim_len = 2
		if self.aim: 
			self.aim_pos = aim
			self.sound = 5
		else: self.aim_pos =	random.choice(self.L_SCREEN),\
								random.choice(self.L_SCREEN)

	def _aim_pos(self):
		self.crash_len *= 0.98
		self.crash_dir += self.change_dir
		if self.aim_len < 8: self.aim_len *= 1.08
		crash = self._vec_x_y(self.crash_dir, self.crash_len)
		aim_dir_len = self._vec(self._vec_sub(self.aim_pos, self.pos))
		aim = self._vec_x_y(aim_dir_len[0], self.aim_len)
		self.rot_dir += 8 * self.change_dir

		if aim_dir_len[1] > 5:
			self.plus = self._vec_add(aim, crash)
			self.pos = self._vec_add(self.pos, self.plus)
			self.image = pygame.transform.rotozoom(self.src_img, self.rot_dir, 1)
		else: 
			self.pos = self.aim_pos
			if self.aim: self.image = self.poem_img
			self.aim_pos = 0
			self.snd._play(self.sound)

class Game_Over(pygame.sprite.Sprite, vector.Vector, Txt, Color):
	def __init__(self, pos_list):
		pygame.sprite.Sprite.__init__(self)
		self.aim_pos = pos_list[1]
		self.fnt = pygame.font.Font(self.font, self.sz_big)
		self.image = self.src_img = self.fnt.render(pos_list[0], True, self.grew_2)
		self.rect = self.image.get_rect()
		self.crash_dir = random.randrange(360)
		self.change_dir = random.choice([-4, 4])
		self.crash_len = 18
		self.aim_len = 2
		self.pos = self.rot_dir = 0

	def update(self, pos):
		if not self.pos: self.pos = pos
		self._go()
		self.image = pygame.transform.rotozoom(self.src_img, self.rot_dir, 1)
		self.rect = self.image.get_rect()
		self.rect.center = self.pos

	def _go(self):
		aim_dir_len = self._vec(self._vec_sub(self.aim_pos, self.pos))
		if aim_dir_len[1] > 5:
			self.crash_len *= 0.98
			self.crash_dir += self.change_dir
			if self.aim_len < 8: self.aim_len *= 1.08
			crash = self._vec_x_y(self.crash_dir, self.crash_len)
			aim = self._vec_x_y(aim_dir_len[0], self.aim_len)
			self.rot_dir += 8 * self.change_dir
			self.plus = self._vec_add(aim, crash)
			self.pos = self._vec_add(self.pos, self.plus)			
		else: 
			self.pos = self.aim_pos
			self.rot_dir = 0


