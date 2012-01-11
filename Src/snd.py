import pygame
from pygame import mixer
from data import Snd

class Sound(Snd):
	def __init__(self):
		self.snd = 0
		pygame.mixer.init(22000, 8, 0, 2048)
		self.arrow_snd = pygame.mixer.Sound(self.arrow_snd)
		self.bug_snd = pygame.mixer.Sound(self.bug_snd)
		self.get_snd = pygame.mixer.Sound(self.get_snd)
		self.fall_snd = pygame.mixer.Sound(self.fall_snd)
		self.final_snd = pygame.mixer.Sound(self.final_snd)

	def _snd(self):
		if self.snd: self.snd = 0
		else: self.snd = 1

	def _play(self, nr):
		if self.snd:
			if nr == 1: self.arrow_snd.play()
			elif nr == 2: self.bug_snd.play()
			elif nr == 3: self.get_snd.play()
			elif nr == 4: self.fall_snd.play()
			elif nr == 5: self.final_snd.play()

