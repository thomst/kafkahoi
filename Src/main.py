"""
This game is written and created by Thomas Leichtfuss

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

This program runs with python 2.6.4 and pygame.
For Windows available at:
http://www.python.org/ftp/python/2.6.4/python-2.6.4.msi
http://pygame.org/ftp/pygame-1.9.1.win32-py2.6.msi
"""

import pygame, math, sys
from pygame.locals import *
import game, snd, start, bug_2, editor
from data import Screen, Background, Sprites

import sqlite3
import Tkinter as tk
import tkMessageBox

class Main(Screen, Background, Sprites):
	def __init__(self):
		self.screen = pygame.display.set_mode(self.SCREEN)
		self.black = pygame.image.load(self.black_img)
		pygame.display.set_caption('Kafkahoi')
		icon = pygame.image.load(self.icon)
		pygame.display.set_icon(icon)
		pygame.font.init()
		self.clock = pygame.time.Clock()
		self.sound = snd.Sound()
		self._bug()
		self.start = start.Start(self.screen, self.black)
		self.start.set_start(self.sound, self.bug_group)
		self.game = game.Game(self.screen, self.black)
		self.action = 0
		self.go = 1
		self.main()

	def _bug(self):
		self.bug_group = pygame.sprite.OrderedUpdates()
		self.bug = bug_2.Bug(self.bug_img)
		for x in range(6):
			self.bug_group.add(bug_2.Legs(self.bug.pos, self.bug.dir, *self.dt_legs[x]))
		self.bug_group.add(bug_2.Feeler(*self.dt_feeler[0]))
		self.bug_group.add(bug_2.Feeler(*self.dt_feeler[1]))
		self.bug_group.add(self.bug)

	def _action(self, action, mouse_pos=0):
		if action == 0:
			self.start.set_start(self.sound, self.game.bug_group)
		elif action == 1: 
			self.game._mouse_pos(mouse_pos)
			self.game.set_game(self.sound, self.start)
			pygame.event.set_grab(True)
		self.action = action

	def main(self):
		while 1:
			self.clock.tick(30)
			for event in pygame.event.get():
				down = event.type == KEYDOWN
				if event.type == QUIT: sys.exit(0)
				if hasattr(event, 'key') and down:
#					print(event.key)
					if event.key == 27: sys.exit(0)
				if self.action == 0: self._start(event, down)
				else: self._play(event, down)
			if self.action == 0: self.start._render()
			elif self.action == 1 and self.go: self.game.go()
			pygame.display.flip()

	def _start(self, event, down):
		if event.type == MOUSEBUTTONDOWN: self._action(1, event.pos)
		if down:
			if event.key == 112: self.start._poem()
			if event.key == 100: self.start._rating()
			if event.key == 115: self.start._snd()
			if event.key == 101:
				editor.Main()
				self.__init__()

	def _play(self, event, down):
		if down and event.key == 112: self._go()
		if event.type == MOUSEMOTION: self.game._mouse_pos(event.pos)
		if self.go:
			if not self.game.done:
				if hasattr(event, 'key'): self.game.key(event, down)
				if event.type == MOUSEBUTTONDOWN: self.game.mousebuttondown(event)
				if event.type == MOUSEBUTTONUP: self.game.mousebuttonup(event)
			elif event.type == MOUSEBUTTONDOWN and self.game.b_rect.collidepoint\
				(event.pos): self._action(0)
			elif pygame.event.get_grab(): pygame.event.set_grab(False)

	def _go(self):
		if self.go: 
			self.go = 0
			pygame.event.set_grab(False)
		else: 
			self.go = 1
			pygame.event.set_grab(True)

