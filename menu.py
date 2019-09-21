import pygame
import sys,os

class MenuButton:

	def __init__(self, text, on_press_callback = None):
		self.text = text
		self.on_press_callback = on_press_callback

class Menu:

	def __init__(self, screen, background_image, buttons):
		self.screen = screen
		self.background_image = background_image
		self.buttons = buttons
		self.font_menu=pygame.font.SysFont('DejaVu Serif',50, True)
		self.active_button=0
		self.coordinates=[]
	def render(self):
		active_button_color = (255,255,0)
		inactive_button_color = (0,0,255)
		dim = self.screen.get_size()

		images = []

		for i,b in enumerate(self.buttons):
			if self.active_button == i:
				images.append(self.font_menu.render(b.text,1 ,active_button_color))
			else:
				images.append(self.font_menu.render(b.text,1 ,inactive_button_color))

		self.screen.blit(self.background_image,(0,0))
		
		total_height = sum([i.get_size()[1] for i in images])
		current_height_increment = 0
		self.coordinates = []
		for i in images:
			x = dim[0]/2 - i.get_size()[0]/2
			y = dim[1]/2 - total_height/2 + current_height_increment
			current_height_increment += i.get_size()[1]
			self.coordinates.append((x,y))
			self.screen.blit(i,(x,y))
		
		pygame.display.flip()

	def get_item(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit(0) 
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						self.active_button -= 1
					if event.key == pygame.K_DOWN:
						self.active_button += 1

					if self.active_button >= len(self.buttons):
						self.active_button = 0

					if self.active_button < 0:
						self.active_button = len(self.buttons)-1

					if event.key == pygame.K_RETURN:
						if self.buttons[self.active_button].on_press_callback:
							self.buttons[self.active_button].on_press_callback(self.buttons[self.active_button])
							continue

						return self.buttons[self.active_button]

				
				self.render()
				mouse_pos = pygame.mouse.get_pos()
				print (mouse_pos)
				if mouse_pos[0]>self.coordinates[0][0] and self.coordinates[0][1]<=mouse_pos[1]<=self.coordinates[0][1]+58:
					self.active_button = 0
					if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
						False

				if mouse_pos[0]>self.coordinates[0][0] and self.coordinates[1][1]<=mouse_pos[1]<=self.coordinates[1][1]+58:
					self.active_button = 1
					if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
						sys.exit()
				#return self.buttons[self.active_button]'''
				


