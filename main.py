import mysql.connector
import os

# Connect to the database
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
