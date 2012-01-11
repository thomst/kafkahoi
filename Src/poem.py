from data import Screen
import sqlite3
import codecs

class Poem(Screen):
	def set_poem(self, poem, size=1):
		self.set_dist(size)

		if poem == 'Game Over': txt = poem
		else:
			curs = sqlite3.connect('db').cursor()
			curs.execute('select poem from poems where title=?', (poem,))
			txt = curs.fetchone()[0]
			curs.close()

		self.make_list(txt)
		self.set_pos()
		self.set_rect()
		self.make_chars()
		self.make_words()

	def set_dist(self, size):
		if size == 1:
			self.dist_col = 12
			self.dist_line = 20
		elif size == 2:
			self.dist_col = 26
			self.dist_line = 20

	def make_list(self, poem):
		self.list = []
		y = z = w = 0
		for x in range(len(poem)):
			if not poem[x] in (' ', '\n', ',', '.'):
				self.list.append([poem[x], (y, z), w])
			if poem[x] in (',', '.'): self.list[-1][0] = poem[x-1] + poem[x]
			if poem[x] == ' ' or poem[x] == '\n' and not poem[x-1] == '\n':
				w += 1
			if poem[x] == '\n': 
				z += 1
				y = -1
			y += 1

	def set_pos(self):
		line = self.list[-1][1][1]
		col = 0
		for x in self.list:
			if col < x[1][0]: col = x[1][0]

		self.width = col * self.dist_col
		self.height = line * self.dist_line
		self.left = self.SCREEN[0]/2 - self.width/2
		self.top = self.SCREEN[1]/2 - self.height/2
		
		self.cols = range(self.left, 1 + self.left + col * self.dist_col, self.dist_col)
		self.lines = range(self.top, 1 + self.top + line * self.dist_line, self.dist_line)

	def set_rect(self):
		left = self.left - 3
		top = self.top - 23
		width = self.width + 25
		height = self.height + 28
		self.dt_rect = ((left, top), (width, height))

	def make_chars(self):
		self.pos_list = []
		for x in range(len(self.list)):
			y = [self.list[x][0],
				(self.cols[self.list[x][1][0]], self.lines[self.list[x][1][1]]),
				self.list[x][2]]
			self.pos_list.append(y)
		self.chars = list(zip(*self.pos_list)[0])

	def make_words(self):
		self.words = []
		for x in range(self.pos_list[-1][2]+1):
			self.words.append([])
			for y in self.pos_list:
				if x == y[2]:
					self.words[x].append(y)

#################
	def col_average(self, poem):
		c_list = [0 for x in range(poem[-1][1][1]+1)]
		for x in range(len(poem)):	
			y = poem[x][1][1]
			if c_list[y] < poem[x][1][0]: c_list[y] = poem[x][1][0]
		c_list = [x for x in c_list[:] if not x == 0]
		c_su = col = 0
		for x in c_list: c_su += x
		c_av = c_su/len(c_list)
		return(c_av)
