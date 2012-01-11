
class Set:
	def set_rating(self, rating):
		if rating == 0: self._1()
		if rating == 1: self._2()
		if rating == 2: self._3()

	def _1(self):
		self.set_fly = 800
		self.set_fly_speed = 4
		self.set_live = 2
		self.set_live_nr = 18

	def _2(self):
		self.set_fly = 700
		self.set_fly_speed = 5
		self.set_live = 3
		self.set_live_nr = 15

	def _3(self):
		self.set_fly = 600
		self.set_fly_speed = 6
		self.set_live = 4
		self.set_live_nr = 12
