import random 
from random import choice
class SimpleAI:
	def __init__(self,player,enemy,field):
		self.player = player
		self.enemy = enemy
		self.field = field
		

	def step(self):
		move = ["up","down","left","right"]
		if self.player.x < self.enemy.x:
			if self.enemy.move("up", self.field.can_move_to) == False:
				return random.choice(move)
		if self.player.x > self.enemy.x:
			if self.enemy.move("down", self.field.can_move_to)== False:
				return random.choice(move)
		if self.player.y < self.enemy.y:
			if self.enemy.move("left", self.field.can_move_to)== False:
				return random.choice(move)
		if self.player.y > self.enemy.y:
			if self.enemy.move("right", self.field.can_move_to)== False:
				return random.choice(move)

	



