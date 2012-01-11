from data import Screen, Poem

class Level(Screen, Poem):
	def set_level(self, level):
		if level == 0: poem = self.poem_1
		elif level == 1: poem = self.poem_2
		elif level == 2: poem = self.poem_3

		dist_col = 12
		dist_line = 20

		line = poem[-1][1][1]
		c_list = [0 for x in range(line+1)]
		for x in range(len(poem)):	
			y = poem[x][1][1]
			if c_list[y] < poem[x][1][0]: c_list[y] = poem[x][1][0]
		c_list = [x for x in c_list[:] if not x == 0]
		c_su = col = 0
		for x in c_list: c_su += x
		c_av = c_su/len(c_list)
		for x in c_list:
			if col < x: col = x

		width = c_av * dist_col
		height = line * dist_line
		left = self.SCREEN[0]/2 - width/2
		top = self.SCREEN[1]/2 - height/2
		
		cols = range(left, 1 + left + col * dist_col, dist_col)
		lines = range(top, 1 + top + line * dist_line, dist_line)

		po = []
		for x in range(len(poem)):
			po.append([poem[x][0],\
			(cols[poem[x][1][0]], lines[poem[x][1][1]]), poem[x][2]])

		words = []
		for x in range(po[-1][2]):
			words.append([])
			for y in po:
				if x == y[2] -1:
					words[x].append(y)

		return(list(zip(*po)[0]), words)

