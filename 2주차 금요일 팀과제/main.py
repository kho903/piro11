# menu ->  character 생성 -> while loop 전투
# 						    hp check, death

import character
import monster
import battle
import os

#menu
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
while True:

	c = None
	while True:
		# asssign character
		if c == None:
			c = start_game()

		# choose action
		# 1: battle 2: upgrade
		print('\nchoose action:\n1. battle  2. upgrade item 3.cash')
		action = input()
		if action == '1':
			print('-------------battleeeeee-------------')
			battle.battle(c)
		if action == '2':
			print('\nchoose action:\n1.item  2. armor')
			action2 = input()
			if action2 =='1':
				cc = int(input('how much?'))
				c.item_strengthen(cc)
			if action2 =='2':
				cc = int(input('how much?'))
				c.armor_strengthen(cc)
		if action == '3':
			a = int(input('how much? '))
			c.cash_charge(a)
		# if action=='4':
		# 	character.shop()
		# check for game end
		if c.hp <= 0:
			print('\n\n\n-------------GAME OVER-------------\n\n\n')
			break
	aa = input('다시하시겠습니까?\n1.yes\n2.no\n')
	if aa == '1':
		continue
	elif aa == '2':
		break

