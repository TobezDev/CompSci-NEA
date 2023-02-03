import mysql.connector
import os

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password=os.getenv("SQL_PASSWORD"),
    database="adventure_game"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS inventory (
    item VARCHAR(255) NOT NULL
);
""")
cursor.execute("""
CREATE TABLE IF NOT EXISTS location (
    place VARCHAR(255) NOT NULL
);
""")
conn.commit()

cursor.execute("INSERT INTO location (place) VALUES ('forest')")
conn.commit()

def get_location():
    cursor.execute("SELECT place FROM location")
    return cursor.fetchone()[0]

def update_location(place):
    cursor.execute("UPDATE location SET place = %s", (place,))
    conn.commit()

def add_item(item):
    cursor.execute("INSERT INTO inventory (item) VALUES (%s)", (item,))
    conn.commit()

def get_inventory():
    cursor.execute("SELECT item FROM inventory")
    return [item[0] for item in cursor.fetchall()]

while True:
    location = get_location()
    print("You are in the " + location)
    print("What would you like to do?")
    print("1. Move")
    print("2. Pick up item")
    print("3. Check inventory")
    print("4. Quit")
    choice = int(input("> "))
    if choice == 1:
        print("Where would you like to go?")
        print("1. Forest")
        print("2. Cave")
        print("3. Beach")
        destination = int(input("> "))
        if destination == 1:
            update_location("forest")
        elif destination == 2:
            update_location("cave")
        elif destination == 3:
            update_location("beach")
    elif choice == 2:
        item = input("What item would you like to pick up? ")
        add_item(item)
    elif choice == 3:
        inventory = get_inventory()
        print("You have:")
        for item in inventory:
            print(item)
    elif choice == 4:
        break

conn.close()

story = f"You are approached by a man, he says he is the head of the {Data['location']}. Do you trust him? (y/n)"
colprint('green', story)

yn = input(">>> ")
if yn[0].lower == 'y':
	if Data['difficulty'][0].lower() == 'e':
		colprint(
		 'green',
		 "He is friendly. He offeres you a drink. You sit with him and discuss the event..."
		)
		colprint(
		 'green',
		 "The Man: Very strange, this. Only us in this massively popular place, what happened?"
		)
		colprint('green', "You: I don't know, seems to be a major event...")
		colprint('green', "You both start conspiring...")
	elif Data['difficulty'][0].lower() == 'm':
		colprint(
		 'green',
		 "He is sociable. He offeres you a coffee. You sit with him and discuss the event..."
		)
		colprint(
		 'green',
		 "The Man: Very strange, this. Only us in this massively popular place, what happened?"
		)
		colprint('green', "You: I don't know, seems to be a major event...")
		colprint('green', "You both start conspiring...")
	elif Data['difficulty'][0].lower() == 'h':
		rI = random.randint(1, 2)  # random chance to be killed by the man (50%)
		if rI == 1:
			colprint(
			 'green',
			 "He is unsociable but, out of shock, offeres you a drink. You sit with him and discuss the event..."
			)
			colprint(
			 'green',
			 "The Man: Very strange, this. Only us in this massively popular place, what happened?"
			)
			colprint('green', "You: I don't know, seems to be a major event...")
			colprint('green', "You both start conspiring...")
		elif rI == 2:
			colprint('orange', "You falsely trusted the man. He was not friendly.")
			player_died()
	elif Data['difficulty'][0].lower() == 'i':
		rI = random.randint(1, 10)  # random chance to be killed by the man (80%)
		if rI > 2:
			colprint(
			 'orange',
			 "He is not sociable in any way. He offeres you a drink and leaves.")
			colprint('orange', "You wonder what you did wrong...")
		else:
			colprint('orange', "You falsely trusted the man. He was not friendly.")
			player_died()
elif yn[0].lower() == 'n':
	if Data['difficulty'][0].lower() == 'e':
		#easy
		pass
	elif Data['difficulty'][0].lower() == 'm':
		#med
		pass
	elif Data['difficulty'][0].lower() == 'h':
		rI = random.randint(1,2)
		pass
	elif Data['difficulty'][0].lower() == 'i':
		rI = random.randint(1,10)
		pass

