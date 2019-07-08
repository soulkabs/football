from getkey import getkey, keys


class Field:
	m = []

	def __init__(self, x,y):
		self.m = [ ["#" for j in range(0, y)] for i in range(0, x)]

	def sets(self, a,x,y):
		self.m[x][y]=a

	def clear(self, x,y):
		pass

	def printt(self):
		for row in self.m:
			for element in row:
				print(element,)
			print("")

class Player:
	s=None

	x=None
	y=None

	def __init__(self, s, x, y):
		self.s = s
		self.x = x
		self.y = y

	def move (self, direction):
		if direction == "up":
			self.x -= "1" 
		if direction == "down":
			self.x += "1" 
		if direction == "left":
			self.y -= "1" 
		if direction == "right":
			self.y += "1" 
		


field = Field(11,15)

player1=Player("a",5,9)
player2=Player("b",5,10)

while True:
	
	key=getkey()
	if key == keys.UP:
			player1.move("up")
	if key == keys.DOWN:
			player1.move("down")
	if key == keys.RIGHT:
			player1.move("right")
	if key == keys.LEFT:
			player1.move("left")

        if key == keys.W:
			player2.move("up")
	if key == keys.S:
			player2.move("down")
	if key == keys.D:
			player2.move("right")
	if key == keys.A:
			player2.move("left")

	field.sets(player1.s,player1.x,player1.y)
	field.sets(player2.s,player2.x,player2.y)
	field.printt()
