import math
from data import Screen

class Vector(Screen):
	def _vec(self, vec):
		return(self._vec_direct(vec), self._vec_len(vec))

	def _vec_direct(self, vec):
		#beginnt oben und zaehlt gegen den Uhrzeigersinn
		if vec[0] < 0:
			self.vec_direct = (math.degrees(math.acos(-vec[1]/(vec[1]**2 + vec[0]**2)**0.5)))
		elif vec[0] != 0 or vec[1] != 0:
			self.vec_direct = 360 - \
				(math.degrees(math.acos(-vec[1]/(vec[1]**2 + vec[0]**2)**0.5)))
		else: self.vec_direct = 0
		return(self.vec_direct)

	def _vec_len(self, vec):
		self.vec_len = ((vec[0]**2 + vec[1]**2)**0.5)
		return(self.vec_len)

	def _vec_x_y(self, direct, lenght):
		#beginnt oben und zaehlt gegen den Uhrzeigersinn
		self.vec_x = -math.sin(math.radians(direct)) * lenght
		self.vec_y = -math.cos(math.radians(direct)) * lenght
		self.vec_koor = (self.vec_x, self.vec_y)
		return(self.vec_koor)

	def _vec_add(self, vec_1, vec_2, vec_3=(0,0)):
		self.vec_koor = [vec_1[x] + vec_2[x] + vec_3[x]for x in (0, 1)]
		return(self.vec_koor)

	def _vec_sub(self, vec_1, vec_2):
		self.vec_koor = [vec_1[x] - vec_2[x] for x in (0, 1)]
		return(self.vec_koor)

	def _vec_multi(self, vec, factor):
		self.vec_koor = (vec[0] * factor, vec[1] * factor)
		return(self.vec_koor)

	def _vec_cor(self, pos, cor_factor, exp, dist_qou):
		vec = self._vec_sub((self.SCREEN[0]/2, self.SCREEN[1]/2), pos)
		dir_len = self._vec(vec)
		dist = self.SCREEN[0]/dist_qou
		if dir_len[1] > dist: cor = cor_factor * (dir_len[1] - dist)**exp
		else: cor = 0
		vec_cor = self._vec_x_y(dir_len[0], cor)
		return(vec_cor)

	def _vec_done(self, pos):
		vec = self._vec_sub(pos, (self.SCREEN[0]/2, self.SCREEN[1]/2))
		dir_len = self._vec(vec)
		if dir_len[1] < 500: cor = 0.0002 * dir_len[1]**2
		else: cor = 0
		vec_cor = self._vec_x_y(dir_len[0], cor)
		return(vec_cor)

	def _vec_angle(self, angle):
		if angle >= 0: new = angle - (360 * (int(angle)/360))
		else: new = angle + (360 * (int(-angle)/360 + 1))
		return(new)
