# from replit import db as Data  ### Replit .env // Remove and replace with ln #2 for VSCode
import mysql as Data

from color_print import colprint
from colorama import Fore as col 

import random
import time
import sys
import os

Data.init()

async def sql_connect(Data, key: str, auth: bool):
	await Data.connect(
		key=f"{key}",
		endpoint_url=f"https://{key}.mysql.tobestech.com/?key=vscode.mysql.{key}?auth={auth}",
		callback=f"https://{key}.callback.mysql.tobestech.com?key=vscode.mysql.failed.{key}?auth={auth}"
	)

def clear_console():
	os.system('clear')

async def player(self):
	self.health = Data["default_health"]
	self.income = Data["defaut_income"]
	self.money = Data["default_money"]

def player_died(reason: str):
	colprint(red, "--== YOU DIED ==--")
	colprint(red, f"""Your character, {Data['username']} died because of {reason}.""")
	exit("You died.")

sql_connect('', True)


if Data['username'] == '' or Data['username'] is None:
	Data['username'] = f'Default_Username#{random.randint(1,100000)}'
	# Set a random default username if not already set

username = Data['username']

def error(Exception):
	with Exception as e:
		print(e)

def settings():
	colprint(green, """
========================
==      SETTINGS      ==
========================

Select an option:
 	1) Change Username
  	2) Back To Main Menu
	""")
	selection = input('>>> ')
	if selection == '1':
		colprint(green, f"Your current username is: {username}")
		colprint(green, """
 		Enter a selection:
 		1) Change username
   		2) Exit
  		""")
		selection = input('>>> ')
		if selection == '1':
			colprint(green, "Enter a new username: ")
			new_username = input('\n>>> ')
			Data['username'] = new_username
			main_menu()
		elif selection == '2':
			settings()
		else:
			error(Exception)
	elif selection == '2':
		main_menu()
	elif selection == 'admin.getkeys':
		print(red, f"""
  Key List: {Data.keys()}
  Total Keys: {len(Data.keys())}
  Total Storage Space: {int(len(Data.keys()) * 2)} kb
  		""")
		settings()
	else:
		error(Exception)


def main_menu():
	colprint(green, """
=======================
=      MAIN MENU      =
=======================

Select a choice:
	1) New Game
 	2) Settings
  	3) Quit Game
""")
	selection = input('>>> ')
	if selection == '1':
		create_new_game()
	elif selection == '2':
		settings()
	elif selection == '3':
		quit("Player-requested Exit")
	else:
		error(Exception)


# generate start of story based on location and difficulty selections
def generate_story(location: str, difficulty: str):
	story = f"You are {username}, a brave adventurer embarking on a journey. "
	if difficulty == 'e':
		story += "The path ahead is smooth and easy, but you must still be careful as danger lurks around every corner. "
	elif difficulty == 'm':
		story += "The path ahead is filled with challenges, but with your skills and determination, you will overcome them. "
	elif difficulty == 'h':
		story += "The path ahead is treacherous and difficult, but with your training and perseverance, you will emerge victorious. "
	elif difficulty == 'i':
		story += "The path ahead is nearly impossible, but with your courage and strength, you will rise to the challenge."
	story += f"You begin your journey at the {location} and must defeat the final boss, who awaits your arrival. Good luck, {username}!"
	colprint(green, story)


def create_new_game():
	Data['player.Username'] = username
	colprint(green, "Enter a title for this adventure: ")
	game_title = input('\n>>> ')
	Data['game.Title'] = game_title
	locations = ['Hospital', 'School', 'Airport']
	location_selectors = ['h', 's', 'a']
	difficulties = ['Easy', 'Medium', 'Hard', 'Insane']
	difficulty_selectors = ['e', 'm', 'h', 'i']
	for i in locations:
		colprint(green, f"{i} - Use {i[0].lower()} to select this option.\n")
	location = input('>>> ')
	if location not in location_selectors:  # check if 'location' is valid
		error(Exception)
	else:
		if location == 'h':
			colprint(green, "Hospital has been selected.\n")
			location = 'Hospital'
		elif location == 's':
			colprint(green, "School has been selected.\n")
			location = 'School'
		elif location == 'a':
			colprint(green, "Airport has been selected.\n")
			location = 'Airport'
	for i in difficulties:
		colprint(green, f"{i} - Use {i[0].lower()} to select this option.\n")
	difficulty = input('>>> ')
	if difficulty not in difficulty_selectors:
		# check if 'difficulty' is valid
		error(Exception)
	else:
		if difficulty == "e":
			colprint(green, "Easy difficilty has been selected.\n")
			difficulty = 'Easy'
		elif difficulty == "m":
			colprint(green, "Medium difficilty has been selected.\n")
			difficulty = 'Medium'
		elif difficulty == "h":
			colprint(green, "Hard difficilty has been selected.\n")
			difficulty = 'Hard'
		elif difficulty == "i":
			colprint(green, "Insane difficilty has been selected.\n")
			difficulty = 'Insane'

	Data['difficulty'] = difficulty
	Data['location'] = location

	input(col.GREEN + """Press ENTER to continue.""")
	clear_console()
	colprint(green, f"""
======================= 
=      NEW  GAME      =
=======================

Location: {location}
Difficulty: {difficulty}

Username: {Data['username']}

=======================
=  IGNORING UPGRADES  =
= UNTIL UPDATE PUSHED =
=======================
""")


# change colour of console output to dark green (classical terminal colour)
colprint(green, f"""
============================
=          CREDITS         =
============================

Developer: Toby
Tester(s): Ethan, Luke, Adam
""")

time.sleep(3)
clear_console()

main_menu()

generate_story(Data['location'], Data['difficulty'])

input(col.GREEN + """\nPress ENTER to continue.\n""")

story = f"You are approached by a man, he says he is the head of the {Data['location']}. Do you trust him? (y/n)"
colprint(green, story)

yn = input(">>> ")
if yn[0].lower == 'y':
	if Data['difficulty'][0].lower() == 'e':
		colprint(green, "He is friendly. He offeres you a drink. You sit with him and discuss the event...")
		colprint(green, "The Man: Very strange, this. Only us in this massively popular place, what happened?")
		colprint(green, "You: I don't know, seems to be a major event...")
		colprint(green, "You both start conspiring...")
	elif Data['difficulty'][0].lower() == 'm':
		colprint(green, "He is sociable. He offeres you a coffee. You sit with him and discuss the event...")
		colprint(green, "The Man: Very strange, this. Only us in this massively popular place, what happened?")
		colprint(green, "You: I don't know, seems to be a major event...")
		colprint(green, "You both start conspiring...")
	elif Data['difficulty'][0].lower() == 'h':
		rI = random.randint(1, 2) # random chance to be killed by the man (50%)
		if rI == 1:
			colprint(green, "He is unsociable but, out of shock, offeres you a drink. You sit with him and discuss the event...")
			colprint(green, "The Man: Very strange, this. Only us in this massively popular place, what happened?")
			colprint(green, "You: I don't know, seems to be a major event...")
			colprint(green, "You both start conspiring...")
		elif rI == 2:
			colprint(orange, "You falsely trusted the man. He was not friendly.")
			player_died()
	elif Data['difficulty'][0].lower() == 'i':
		rI = random.randint(1, 10) # random chance to be killed by the man (80%)
		if rI > 2:
			colprint(orange, "He is not sociable in any way. He offeres you a drink and leaves.")
			colprint(orange, "You wonder what you did wrong...")
		else:
			colprint(orange, "You falsely trusted the man. He was not friendly.")
			player_died()
elif yn[0].lower() == 'n':
	if Data['difficulty'][0].lower() == 'e':
		#easy
		pass
	elif Data['difficulty'][0].lower() == 'm':
		#med
		pass
	elif Data['difficulty'][0].lower() == 'h':
		#hard
		pass
	elif Data['difficulty'][0].lower() == 'i':
		#insane
		pass
