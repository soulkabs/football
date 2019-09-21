from copy import deepcopy
from glob import glob
class Field:

	def __init__(self, namefile):
		self.initial_state = []
		self.current_state = []

		f = open( namefile , mode='r')
		string = f.read()
		string = string.strip("\n")
		f.close()
		lst = string.split('\n')
		for elem in lst:
			arr = elem.split()
			self.initial_state.append(arr)
		self.clear()

		self.size_x=len(self.initial_state)
		self.size_y = len(self.initial_state[0])

	def sets(self, a,x,y):
		self.current_state[x][y]=a

	def printt(self):
		for row in self.current_state:
			for element in row:
				print (element,end='')
			print ("")

	def get_starting_position(self):
		return self.find_symbol('S')

	def get_ending_position(self):
		return self.find_symbol('E')

	def find_symbol(self,s):
		for i, _ in enumerate(self.initial_state):
			for j, _ in enumerate(self.initial_state[i]):
				if self.initial_state[i][j] == s:
					return i,j

	def clear(self):
		self.current_state = deepcopy(self.initial_state)

	def can_move_to(self,x,y):
		if self.current_state[x][y] == '!':
			return False
		return True
