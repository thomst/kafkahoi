# -*- coding: utf-8 -*-

import pygame, os
from pygame.locals import *
from data import Background, Txt, Color, Screen
from rating import Rating
from poem import Poem
from text import Text
import sqlite3
from data import DATABASE


class Start(Text, Rating, Poem, Background, Txt, Color, Screen):
	def __init__(self, screen, black):
		self.screen = screen
		self.black = black
		self.black.set_alpha(100)
		self.rect = pygame.Rect((210, 255), (228, 145))
		self.rat = self.poem = 0
		self.pms = []
		self._pms()

		self.txt = [Text(self.ka_txt, self.sz_big, (0,-50), 1)]
		self.l = self.txt[0].rect.width
		self.txt.append(Text(self.mo_txt, self.sz_menu,(-self.l/2+3,-30)))
		self.txt.append(Text(self.p_txt, self.sz_menu, (-self.l/2+3,-10), 0, 1))
		self.txt.append(Text(self.po_txt, self.sz_menu, (-self.l/2+15,-10)))
		self.txt.append(Text(self.d_txt, self.sz_menu, (-self.l/2+3,10), 0, 1))
		self.txt.append(Text(self.di_txt, self.sz_menu, (-self.l/2+15,10)))
		self.txt.append(Text(self.s_txt, self.sz_menu, (-self.l/2+3,30), 0, 1))
		self.txt.append(Text(self.so_txt, self.sz_menu, (-self.l/2+15,30)))
		self.txt.append(Text(self.e_txt, self.sz_menu, (-self.l/2+3,50), 0, 1))
		self.txt.append(Text(self.ed_txt, self.sz_menu, (-self.l/2+15,50)))

		self.txt_group = pygame.sprite.RenderPlain(self.txt)
		self.gr_poem = pygame.sprite.GroupSingle\
			(Text(self.pms[0], self.sz_menu, (self.l/2-5,-10), 2))
		self.gr_rating = pygame.sprite.GroupSingle\
			(Text(str(self.rat + 1), self.sz_menu, (self.l/2-5,10), 2))
		self.gr_snd = pygame.sprite.GroupSingle()

	def _pms(self):
		c = sqlite3.connect(DATABASE).cursor()
		c.execute('select title from poems')

		if hasattr(os, 'uname'):	#spezifisch für Linux
			self.pms = [x[0] for x in c]
		else:						#Windows
			self.pms = [x[0] for x in c]
		c.close()

	def set_start(self, sound, bug_group):
		self.sound = sound
		self.bug_group = bug_group
		self.bug = bug_group.sprites()[-1]
		self.gr_snd.add(Text\
			(self.snd_txt[self.sound.snd], self.sz_menu, (self.l/2-5,30), 2))
		self.background = pygame.image.load(self.background_img)
		self.background.blit(self.black, self.rect.topleft, self.rect)
		self.screen.blit(self.background, (0, 0))

	def _poem(self):
		self.poem += 1
		if self.poem == len(self.pms): self.poem = 0
		self.gr_poem.add(Text(self.pms[self.poem], self.sz_menu, (self.l/2-5,-10), 2))

	def _rating(self):
		if self.rat < 2: self.rat += 1
		else: self.rat = 0
		self.gr_rating.add(Text(str(self.rat + 1), self.sz_menu, (self.l/2-5,10), 2))

	def _snd(self):
		self.sound._snd()
		self.gr_snd.add(Text\
			(self.snd_txt[self.sound.snd], self.sz_menu, (self.l/2-5,30), 2))

	def _render(self):
		self.txt_group.clear(self.screen, self.background)
		self.gr_poem.clear(self.screen, self.background)
		self.gr_rating.clear(self.screen, self.background)
		self.gr_snd.clear(self.screen, self.background)
		self.bug_group.clear(self.screen, self.background)
		self.bug_group.update(self.bug.pos, self.bug.dir)
		self.txt_group.draw(self.screen)
		self.gr_poem.draw(self.screen)
		self.gr_rating.draw(self.screen)
		self.gr_snd.draw(self.screen)
		self.bug_group.draw(self.screen)
