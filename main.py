from getkey import getkey, keys
import sys, os
from copy import deepcopy
from glob import glob
import random
from random import choice
import pygame
import time
import menu 
import field
import player
import enemy
import aicontrollers

'''Создание окна'''
window=pygame.display.set_mode((1024,768))
window_image=pygame.image.load(('game_res/images/menu.jpg'))
screen = pygame.Surface((500,275))

'''Название игры'''
pygame.display.set_caption('MAZE')

"""Шрифты"""
pygame.font.init()
sfont=pygame.font.SysFont('DejaVu Serif',24, True)

'''Sprites for game'''
E=pygame.image.load('game_res/images/portal.png')
E.set_colorkey((255,255,255))
sprites = { '!': pygame.image.load('game_res/images/briks.jpg'), 
			'#': pygame.image.load('game_res/images/field.png'),
			'E': E,
			'S': pygame.image.load('game_res/images/field.png')}

player_sprite = pygame.image.load('game_res/images/hero.jpg')
player_sprite.set_colorkey((255,255,255))
enemy_sprite = pygame.image.load('game_res/images/enemy.png')
enemy_sprite.set_colorkey((255,255,255))

"""Создание меню"""
def process_menu():
	button_start = menu.MenuButton("START")
	button_exit = menu.MenuButton("EXIT")

	mymenu = menu.Menu(window,window_image,[button_start,button_exit])
	selected_button = mymenu.get_item()

	if selected_button == button_exit:
		sys.exit(0)

process_menu()

def mark_player(m,player):
	m.sets(player.s,player.x,player.y)

def get_screen_block_size(sx,sy):
	return screen.get_size()[1]//sx, screen.get_size()[0]//sy

def draw_cart(cart,screen, player, enemys):
	sx, sy = get_screen_block_size(cart.size_x, cart.size_y)
	for i, col in enumerate(cart.current_state):
		for j, e in enumerate(col):
			x = j*sx
			y = i*sy
			screen.blit(pygame.transform.scale(sprites[e],(sx,sy)),(x,y))

	screen.blit(pygame.transform.scale(player_sprite,(sx,sy)), (player.screen_xc-sx//2, player.screen_yc-sy//2))

	for enemy in enemys:
		screen.blit(pygame.transform.scale(enemy_sprite,(sx,sy)),(enemy.screen_xc-sx//2, enemy.screen_yc-sy//2))


l = glob("./game_res/levels/level*.txt")

level = 0
m = None
start_x,start_y = None,None
end_x,end_y = None, None
player1 = None
enemys = []
AIs=[]
pygame.init()

def next_level(levelname):
	global m, start_x,start_y,end_x,end_y,player1,enemys,AIs
	m = field.Field(levelname) 
	start_x,start_y = m.get_starting_position()
	end_x,end_y = m.get_ending_position()

	player1=player.Player("@",start_x,start_y, get_screen_block_size(m.size_x, m.size_y))
	enemys=[enemy.Enemy("%",8,15, get_screen_block_size(m.size_x, m.size_y)),
			enemy.Enemy("%",8,5, get_screen_block_size(m.size_x, m.size_y))]

	AIs = []
	[AIs.append(aicontrollers.SimpleAI(player1,enemy, m)) for enemy in enemys]

'''Подготовка к запуску игры'''
running = True
next_level(l[level])
window.blit(window_image,(0,0))
count=1
'''Игровой цикл'''
while running:
	'''Отрисовка экрана'''
	m.clear()
	window.blit(sfont.render('Уровень:'+ str(count),1,(210,120,10)),(10,5))
	window.blit(screen,(300,200))
	'''Обработчик событий'''
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	if pygame.key.get_pressed()[pygame.K_ESCAPE]:
		process_menu()

	'''Передвижение игрока'''
	if not player1.in_transition():
		key_pressed = pygame.key.get_pressed()
		if pygame.key.get_pressed()[pygame.K_RIGHT]:
			player1.move("right", m.can_move_to)
		if pygame.key.get_pressed()[pygame.K_UP]:
			player1.move("up", m.can_move_to)
		if pygame.key.get_pressed()[pygame.K_DOWN]:
			player1.move("down", m.can_move_to)
		if pygame.key.get_pressed()[pygame.K_LEFT]:
			player1.move("left", m.can_move_to)
	
	player1.update_screen_coords()

	'''Передвижение препятствия'''
	for i in AIs:
		if not i.enemy.in_transition():
			i.step()
		i.enemy.update_screen_coords()

	#if player1.x == enemy.x and player1.y == enemy.y:
	#	next_level(l[level])

	if end_x == player1.x and end_y == player1.y:
		level+=1
		next_level(l[level])
		count+=1

	draw_cart(m,screen,player1, enemys)
	

	pygame.display.flip()
	time.sleep(0.001)

