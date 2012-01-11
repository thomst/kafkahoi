import poem, rating, snd

class Setting(poem.Poem, rating.Rating, snd.Sound):
	def get_set(self, poem, rating):
		self.set_poem(poem)
		self.set_rating(rating)
