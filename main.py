# see .md for more info

from replit import db as Data  # type: ignore
# Built-in .env                > (for VSCode)

from colorama import Fore as col
import random
import time
import sys
import os


def clear_console():
	os.system('clear')


def typingPrint(text):
	for character in text:
		sys.stdout.write(character)
		sys.stdout.flush()
		time.sleep(0.02)


async def player(self):
	self.health = Data["default_health"]
	self.income = Data["defaut_income"]
	self.money = Data["default_money"]


if Data['username'] == '' or Data['username'] is None:
	Data['username'] = f'Default_Username#{random.randint(1,100000)}'
	# Set a random default username if not already set

username = Data['username']


# error handler
def error(Exception):
	with Exception as e:
		print(e)


def settings():
	print("""
========================
==      SETTINGS      ==
========================

Select an option:
 	1) Change Username
  	2) Back To Main Menu
	""")
	selection = input('>>> ')
	if selection == '1':
		print(f"Your current username is: {username}")
		print("""
 		Enter a selection:
 		1) Change username
   		2) Exit
  		""")
		selection = input('>>> ')
		if selection == '1':
			typingPrint("Enter a new username: ")
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
		print(f"""
  Key List: {Data.keys()}
  Total Keys: {len(Data.keys())}
  Total Storage Space: {int(len(Data.keys()) * 2)} kb
  		""")
		settings()
	else:
		error(Exception)


def main_menu():
	print("""
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
		new_game()
	elif selection == '2':
		settings()
	elif selection == '3':
		quit("Player-requested Exit")
	else:
		error(Exception)


# generate start of story based on location and difficulty selections
def generate_story(location, difficulty):
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
	print(story)


def new_game():
	Data['player.Username'] = username
	typingPrint("Enter a title for this adventure: ")
	game_title = input('\n>>> ')
	Data['game.Title'] = game_title
	locations = ['Hospital', 'School', 'Airport']
	location_selectors = ['h', 's', 'a']
	difficulties = ['Easy', 'Medium', 'Hard', 'Insane']
	difficulty_selectors = ['e', 'm', 'h', 'i']
	for i in locations:
		typingPrint(f"{i} - Use {i[0].lower()} to select this option.\n")
	location = input('>>> ')
	if location not in location_selectors:  # check if 'location' is valid
		error(Exception)
	else:
		if location == 'h':
			typingPrint("Hospital has been selected.\n")
			location = 'Hospital'
		elif location == 's':
			typingPrint("School has been selected.\n")
			location = 'School'
		elif location == 'a':
			typingPrint("Airport has been selected.\n")
			location = 'Airport'
	for i in difficulties:
		typingPrint(f"{i} - Use {i[0].lower()} to select this option.\n")
	difficulty = input('>>> ')
	if difficulty not in difficulty_selectors:
		# check if 'difficulty' is valid
		error(Exception)
	else:
		if difficulty == "e":
			typingPrint("Easy difficilty has been selected.\n")
			difficulty = 'Easy'
		elif difficulty == "m":
			typingPrint("Medium difficilty has been selected.\n")
			difficulty = 'Medium'
		elif difficulty == "h":
			typingPrint("Hard difficilty has been selected.\n")
			difficulty = 'Hard'
		elif difficulty == "i":
			typingPrint("Insane difficilty has been selected.\n")
			difficulty = 'Insane'

	Data['difficulty'] = difficulty
	Data['location'] = location

	# save the game's starting data in a decryptable string

	input("""Press ENTER to continue.""")
	clear_console()
	print(f"""
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
print(f"""{col.GREEN}
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

input("""\nPress ENTER to continue.\n""")

story = f"You are approached by a man, he says he is the head of the {Data['location']}. Do you trust him? (y/n)"
print(story)

yn = input(">>> ")
if yn[0].lower == 'y':
	if Data['difficulty'][0].lower() == 'e':
		print(
		 "He is friendly. He offeres you a drink. You sit with him and discuss the event..."
		)
		print(
		 "The Man: Very strange, this. Only us in this massively popular place, what happened?"
		)
		print("You: I don't know, seems to be a major event...")
		print("You both start conspiring...")

	elif Data['difficulty'][0].lower() == 'm':
		print(
		 "He is sociable. He offeres you a drink. You sit with him and discuss the event..."
		)
		print(
		 "The Man: Very strange, this. Only us in this massively popular place, what happened?"
		)
		print("You: I don't know, seems to be a major event...")
		print("You both start conspiring...")
	elif Data['difficulty'][0].lower() == 'h':
		rI = random.randint(1, 2) # random chance to be killed by the man (50%)
		if rI == 1:
			print(
			 "He is unsociable. He, out of shock, offeres you a drink. You sit with him and discuss the event..."
			)
			print(
			 "The Man: Very strange, this. Only us in this massively popular place, what happened?"
			)
			print("You: I don't know, seems to be a major event...")
			print("You both start conspiring...")
		elif rI == 2:
			print("You falsely trusted the man. He was not friendly.")
			print(col.RED + "-= YOU DIED =-")
	elif Data['difficulty'][0].lower() == 'i':
		rI = random.randint(1, 10) # random chance to be killed by the man (80%)
		if rI > 8:
			print("He is not sociable in any way. He offeres you a drink and leaves.")
			print("You wonder what you did wrong...")
		else:
			print("You falsely trusted the man. He was not friendly.")
			print(col.RED + "-= YOU DIED =-")
elif yn[0].lower() == 'n':
	pass
	#if player does not trust the man
