class Player:
	s=None
	x=None
	y=None

	def __init__(self, s, x, y, screen_block_size):
		self.s = s
		self.x = x
		self.y = y
		self.screen_block_size = screen_block_size
		#self.speed = speed
		self.screen_yc = x*screen_block_size[0] + screen_block_size[0]/2
		self.screen_xc = y*screen_block_size[1] + screen_block_size[1]/2
		self.in_transition_ = False;

	def move (self, direction, canmove):
		x,y = self.x, self.y

		if direction == "up":
			x -= 1
		if direction == "down":
			x += 1
		if direction == "left":
			y -= 1
		if direction == "right":
			y += 1

		if canmove(x,y):
			self.x = x
			self.y = y
	
	def in_transition(self):
		return self.in_transition_

	def new_screen_y(self):
		return self.x*self.screen_block_size[0] + self.screen_block_size[0]/2

	def new_screen_x(self):
		return self.y*self.screen_block_size[1] + self.screen_block_size[1]/2

	def update_screen_coords(self):
		if self.screen_xc < self.new_screen_x():
			self.screen_xc += 1
			self.in_transition_ = True
			return
		if self.screen_xc > self.new_screen_x():
			self.screen_xc -= 1
			self.in_transition_ = True
			return

		if self.screen_yc < self.new_screen_y():
			self.screen_yc += 1
			self.in_transition_ = True
			return
		if self.screen_yc > self.new_screen_y():
			self.screen_yc -= 1
			self.in_transition_ = True
			return

		self.in_transition_ = False
		
