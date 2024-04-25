import csv
import psycopg2 as pgsql

# Establish connection
connection = pgsql.connect(
    host="localhost",
    database="phone_numbers",
    user="turanov",
    password="muslim123"
)

# Create a cursor
cur = connection.cursor()

# Create table if not exists
cur.execute("""CREATE TABLE IF NOT EXISTS PhoneBook (
    surname VARCHAR(255),
    name VARCHAR(255),
    number INT
);
""")

# Define update function
def update(sn, mode, newv):
    cur.execute("""UPDATE PhoneBook
    SET {} = %s
    WHERE surname = %s
    """.format(mode), (newv, sn))

# Define delete function
def delete(sn):
    cur.execute("""DELETE FROM PhoneBook
    WHERE surname = %s
    """, (sn,))

# INSERTING DATA--------------------------

mode = "enter"
while True:
    print("Type 'enter' if you want to add more data and type 'stop' to break")
    mode = input()
    if mode == "stop":
        break
    print("Enter surname:")
    surname = input()
    print("Enter name:")
    name = input()
    print("Enter number:")
    number = int(input())
    cur.execute("INSERT INTO PhoneBook (surname, name, number) VALUES (%s, %s, %s)", (surname, name, number))

# Insert data from CSV file
while True:
    print("Want to insert data from a CSV file? yes/no:")
    mode = input()
    if mode == "no":
        break
    print("Enter the name of the file (without the .csv extension):")
    filename = input()
    with open(filename + '.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header row
        for row in reader:
            cur.execute("INSERT INTO PhoneBook (surname, name, number) VALUES (%s, %s, %s)", row)

# UPDATING DATA---------
while True:
    print("Type 'update' to update some data or 'stop' to break")
    mode = input()
    if mode == "stop":
        break
    cur.execute("SELECT * FROM PhoneBook")
    print(cur.fetchall())
    print("Enter surname to update:")
    idtochange = input()
    print("What do you want to change? (name/number)")
    mode = input()
    print("Enter new value:")
    newvalue = input()
    update(idtochange, mode, newvalue)

# DELETING DATA-----------
while True:
    print("Want to delete some data? yes/no")
    mode = input()
    if mode == "no":
        break
    cur.execute("SELECT * FROM PhoneBook")
    print(cur.fetchall())
    print("Enter surname to delete:")
    idtodelete = input()
    delete(idtodelete)

# Commit changes and close cursor and connection
connection.commit()
cur.close()
connection.close()
