#!/usr/bin/env python3.1

import pygame, math, sys, random
from pygame.locals import *
import star_2, bug_2, fly, arrows, letter, lives, vector, setting, poem
from data import Screen, Sprites, Color, Background



class Game(setting.Setting, Screen, Sprites, Color, Background):
	def __init__(self, screen, black):
		self.screen = screen
		self.black = black
		self.over = poem.Poem()
		self.over.set_poem('Game Over', 2)
		self.o_rect = pygame.Rect((203, 307), (244, 40))
		self.back = pygame.image.load(self.back_img)
		self.b_rect = self.back.get_rect()
		self.b_rect.topleft = (580, 580)
		self.k_right = self.k_left = self.right_left = 0
		self.button = 0

	def set_game(self, sound, start):
		self.done = self.letter_nr = self.g_over = self.o_pos = self.alpha = 0
		self.lives = []
		self.move_list = []
		self.background = pygame.image.load(self.background_img)
		self.screen.blit(self.background, (0, 0))
		self.sound = sound
		self.get_set(start.pms[start.poem], start.rat)
		self.bug = start.bug_group.sprites()[-1]
		self.bug_group = start.bug_group
		self.sprites()
		self.rect = pygame.Rect(self.dt_rect)

	def sprites(self):
		self.star_1 = star_2.Star(self.mouse_pos, control=True, *self.dt_star_1)
		self.star_2 = star_2.Star(self.mouse_pos, *self.dt_star_2)
		self.star_group = pygame.sprite.RenderPlain(self.star_1, self.star_2)
		self.arrow_group = pygame.sprite.RenderPlain()
		self.fly_group = pygame.sprite.RenderPlain()
		self.letter_group = pygame.sprite.RenderPlain()
		self.l_group = pygame.sprite.RenderPlain()
		self.m_letter_group = pygame.sprite.RenderPlain()
		self.live_group = pygame.sprite.RenderPlain()
		self.poem_group = pygame.sprite.RenderPlain()
		self.over_group = pygame.sprite.RenderPlain()
		for x in range(25):
			let = letter.Letter(self.chars.pop\
			(random.randrange(len(self.chars))), self.sound)
			self.letter_group.add(let)
		for let in self.chars:
			self.l_group.add(letter.Letter(let, self.sound))
		for x in range(12, 12 + 21 * 25, 21):
			self.lives.append(lives.Lives\
			(self.lives_img, (x, self.SCREEN[1]-12), self.sound)) 
		for x in range(self.live_nr):
			self.live_group.add(self.lives[x])
		for let in self.over.pos_list:
			self.over_group.add(letter.Game_Over(let))

	def handle_lives(self, plus_minus, star=0):
		if plus_minus > 0 and self.live_nr < 25:
			self.live_group.add(self.lives[self.live_nr])
			self.live_nr += 1
		if plus_minus < 0:
			self.live_nr -= 1
			self.live_group.remove(self.lives[self.live_nr])
		if self.live_nr == -1: self.o_pos = star.pos


	def crash_letter(self):
		for let in self.m_letter_group.sprites():
			let._crash_sets()
		self.letter_group.add(self.m_letter_group)
		self.m_letter_group.empty()
		self.letter_nr = 0
		self.move_list = []

	def poem(self, g):
		for let in self.m_letter_group.sprites():
			for x in range(len(g)):
				if let.name == g[x][0]:
					let._crash_sets(g.pop(x)[1])
					break
		self.poem_group.add(self.m_letter_group)
		self.m_letter_group.empty()
		self.letter_nr = 0
		self.move_list = []

	def poem_test(self):
		names = []
		g = []
		for let in self.m_letter_group.sprites():
			names.append(let.name)
		for x in self.words[:]:
			if not x: self.words.remove(x)
		for x in range(len(self.words)):
			n = list(zip(*self.words[x])[0])
			for y in names:
				if y in n: n.remove(y)
				if not n: break
			if not n: 
				g += self.words.pop(x)
			if g: break
		if g:
			n = list(zip(*g)[0])
			for x in n:
				if x in names: names.remove(x)
			for x in range(len(self.words)):
				for y in self.words[x][:]:
					if y[0] in names:
						g.append(y)
						names.remove(y[0])
						self.words[x].remove(y)
			for x in self.words[:]:
				if not x: self.words.remove(x)
			self.poem(g)
		else: self.crash_letter()

	def _cheat(self):
		l = []
		for x in self.words:
			l += [y for y in x]
		for let in self.l_group.sprites():
			for x in range(len(l)):
				if let.name == l[x][0]:
					let._crash_sets(l.pop(x)[1])
					break
		for let in self.letter_group.sprites():
			for x in range(len(l)):
				if let.name == l[x][0]:
					let._crash_sets(l.pop(x)[1])
					break
		for let in self.m_letter_group.sprites():
			for x in range(len(l)):
				if let.name == l[x][0]:
					let._crash_sets(l.pop(x)[1])
					break
		self.words = 0
		self.letter_nr = 0
		self.poem_group.add(self.l_group, self.letter_group, self.m_letter_group)
		self.m_letter_group.empty()
		self.letter_group.empty()
		self.live_group.empty()

##### Events #####

	def key(self, event, down):
		if event.key in (102, 122, 276): self.star_1.right = down
		if event.key in (115, 275): self.star_1.left = down
		if event.key in (32, 274) and down: self.poem_test()
		if self.button and event.key == 97 and down: self._cheat()

	def mousebuttondown(self, event):
		if event.button == 1:
			arrows.Arrow(self.arrow_img, self.star_1.rot_dir, \
							self.star_1.pos).add(self.arrow_group)
			self.sound._play(1)
		if event.button == 3:
			for let in self.letter_group.sprites():
				coll = pygame.sprite.collide_circle(self.star_2, let)
				if coll:
					self.letter_group.remove(let)
					if let.name == 'live':
						self.handle_lives(1)
						self.sound._play(5)
					else:
						self.letter_nr += 1
						let._nr(self.letter_nr)
						self.m_letter_group.add(let)
						self.sound._play(3)
		if event.button == 3: self.button = True
		if self.button:
			if event.button == 4: self.star_2.dir -= 30
			if event.button == 5: self.star_2.dir += 30
		else:
			if event.button == 4: self.star_1.dir += 30
			if event.button == 5: self.star_1.dir -= 30

	def mousebuttonup(self, event):
		if event.button == 3: self.button = 0

	def _mouse_pos(self, mouse_pos):
		self.mouse_pos = mouse_pos

##### go #####

	def collision_bug(self):
		arrows = pygame.sprite.spritecollide(self.bug, self.arrow_group, True)			
		crash_1 = pygame.sprite.collide_circle(self.bug, self.star_1)
		crash_2 = pygame.sprite.collide_circle(self.bug, self.star_2)
		if arrows:
			del(arrows[0])
			self.bug._hit_sets()
			self.sound._play(2)
		if crash_1 or crash_2:
			if crash_1: 
				self.star_1._crash_sets(self.bug.pos)
				self.handle_lives(-1, self.star_1)
			else:
				self.star_2._crash_sets(self.bug.pos)
				self.crash_letter()
				self.handle_lives(-1, self.star_2)
			self.bug._hit_sets()
			self.sound._play(2)

	def collision_fly(self):
		for fly in self.fly_group:
			hits = pygame.sprite.spritecollide(fly, self.arrow_group, True)
			crash_1 = pygame.sprite.collide_circle(fly, self.star_1)
			crash_2 = pygame.sprite.collide_circle(fly, self.star_2)
			if hits:
				self.sound._play(2)
				counter = maxi = 0
				if random.randrange(3) <= 1: maxi = random.randrange(25)
				for let in self.l_group.sprites()[:]:
					if counter == maxi: break
					let._crash_sets(0, fly.pos)
					let.add(self.letter_group)
					let.remove(self.l_group)
					counter += 1
				if random.randrange(self.set_live) < 1:
					live = lives.Lives(self.heart_img, fly.pos, self.sound)
					live._crash_sets(0, fly.pos)
					self.letter_group.add(live)
				self.fly_group.remove(fly)
			if crash_1: 
				self.star_1._crash_sets(fly.pos)
				self.handle_lives(-1, self.star_1)
			if crash_2: 
				self.star_2._crash_sets(fly.pos)
				self.crash_letter()
				self.handle_lives(-1, self.star_2)
			if crash_1 or crash_2:
				self.sound._play(2)

	def delete_arrows(self):
		for arrow in self.arrow_group:
			if not int(arrow.pos[0]) in range(self.SCREEN[0]) \
			or not int(arrow.pos[1]) in range(self.SCREEN[1]):
				self.arrow_group.remove(arrow)

	def fly(self):
		if random.randrange(self.set_fly) < 1:
			fly.Fly(self.set_fly_speed, *self.dt_fly).add(self.fly_group)

	def _move_list(self):
		self.move_list.insert(0, self.star_2.pos)
		if len(self.move_list) > self.letter_nr * 5: self.move_list.pop()

	def go(self):
		if self.letter_nr: self._move_list()
		if self.o_pos: self._over()
		if not self.words: self._done()
		self.render()
		if not self.done:
			if not self.bug.hit: self.collision_bug()
			self.collision_fly()
			self.delete_arrows()
			self.fly()

	def _done(self):
		if not self.done:
			self.background.blit(self.black, self.rect.topleft, self.rect)
			self.screen.blit(self.background, (0, 0))
			self.done = 1

	def _over(self):
		if self.alpha < 100: self.alpha += 2
		self.black.set_alpha(self.alpha)
		self.done = 1

	def render(self):
		self.letter_group.clear(self.screen, self.background)
		self.poem_group.clear(self.screen, self.background)
		self.live_group.clear(self.screen, self.background)
		self.arrow_group.clear(self.screen, self.background)
		self.bug_group.clear(self.screen, self.background)
		self.fly_group.clear(self.screen, self.background)
		self.m_letter_group.clear(self.screen, self.background)
		self.star_group.clear(self.screen, self.background)
		if self.o_pos: 
			self.over_group.clear(self.screen, self.background)
			self.screen.blit(self.background, self.o_rect, self.o_rect)
		if self.done: self.screen.blit(self.background, self.b_rect, self.b_rect)

		self.star_group.update(self.mouse_pos, self.done)
		self.m_letter_group.update(self.move_list)
		self.poem_group.update()
		self.letter_group.update()
		self.bug_group.update(self.bug.pos, self.bug.dir)
		self.fly_group.update(self.done)
		self.arrow_group.update()
		if self.o_pos: self.over_group.update(self.o_pos)

		self.poem_group.draw(self.screen)
		self.letter_group.draw(self.screen)
		self.live_group.draw(self.screen)
		if self.o_pos:
			self.screen.blit(self.black, self.o_rect, self.o_rect)
			self.over_group.draw(self.screen)
		self.bug_group.draw(self.screen)
		self.m_letter_group.draw(self.screen)
		self.arrow_group.draw(self.screen)
		self.fly_group.draw(self.screen)
		self.star_group.draw(self.screen)
		if self.done: self.screen.blit(self.back, (580, 580))
		#pygame.draw.circle(self.screen, (255, 255, 255), (580, 580), 2)

