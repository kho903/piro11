# menu ->  character 생성 -> while loop 전투
# 						    hp check, death

import character
import monster
import battle
import os

#menu
c = None
def start_game():
	print('''\
	select option:
	1. make chararcter
	2. select character
	 ''')
	option = input()
	if option == '1':
		c = character.User()
	return c

#main
c = None
while(True):
	# asssign character
	if c == None:
		c = start_game()

	# choose action
	# 1: battle 2: upgrade
	print('\nchoose action:\n1. battle  2. upgrade item')
	action = input()
	if action == '1':
		print('battleeeeee')
		battle.battle(c)
	if action == '2':
		c.item_strengthen()
		pass

	# check for game end
	if c.hp <= 0:
		print('\n\n\n-------------GAME OVER-------------')
		break