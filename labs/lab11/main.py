import psycopg2
import csv
from config import host, user, password, database_name
from psycopg2 import Error

conn = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=database_name
)

conn.autocommit = True

cursor = conn.cursor()

def createtable():
    sql = '''
        CREATE TABLE IF NOT EXISTS phone(
        name VARCHAR(255),
        number VARCHAR(20)
    )
    '''
    cursor.execute(sql)


def insertdata():
    name = input("Name to insert: ")
    number = input("Number to insert: ")
    sql = '''
   INSERT INTO phone(name, number) VALUES
   (%s, %s)
'''
    cursor.execute(sql, (name, number))


def insertfromcsv():
    with open("C:\\Users\\musli\\Documents\\pp2\\PP2\\labs\\lab10\\que.csv", 'r') as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            if len(row) >= 2:  
                sql = '''
                    INSERT INTO phone(name, number) VALUES
                    (%s, %s)
                    '''
                cursor.execute(sql, (row[0], row[1]))
            else:
                print("Skipping row with insufficient data:", row)



def updatedatabyname():
    find = input("Enter a name to find: ")
    update = input("Enter a new number: ")
    sql = '''
    UPDATE phone SET number = %s WHERE name = %s
    '''
    cursor.execute(sql, (update, find))


def updatedatabynumber():
    find = input("Enter a number to find: ")
    update = input("Enter a new name: ")
    sql = '''
    UPDATE phone SET name = %s WHERE number = %s
    '''
    cursor.execute(sql, (update, find))


def deletedatabyname():
    find = input("Enter a name to delete: ")
    sql = '''
    DELETE FROM phone WHERE name = %s
    '''
    cursor.execute(sql, (find,))


def deletedatabynumber():
    find = input("Enter a number to delete: ")
    sql = '''
    DELETE FROM phone WHERE number = %s
    '''
    cursor.execute(sql, (find,))


def byletter():
    find = input("Enter first letter of name to find: ")
    sql = '''
    SELECT * FROM phone WHERE name LIKE %s
    '''
    cursor.execute(sql, (find + '%',))
    records = cursor.fetchall()
    for record in records:
        print(record)


# createtable()
# insertdata()
# insertfromcsv()
# updatedatabyname()
# updatedatabynumber()
# deletedatabyname()
# byletter()

# LAB11:
def partialname():
    find = input("Enter partial name to find: ")
    sql = "SELECT * FROM phone WHERE name LIKE %s"
    cursor.execute(sql, ('%' + find + '%',))
    records = cursor.fetchall()
    for record in records:
        print(record)


def deletedatabynumber():
    find = input("Enter a number to delete ")
    sql = f'''
    DELETE FROM phone WHERE number = '{find}';
    '''
    cursor.execute(sql)

def add_users():
    contacts = []
    
    num_contacts = int(input("Enter the number of contacts you want to add: "))
    
    for _ in range(num_contacts):
        name = input("Enter name: ")
        number = input("Enter number: ")
        contacts.append((name, number))
    
    try:
        for contact in contacts:
                cursor.execute('INSERT INTO phone(name, number) VALUES (%s, %s)', (contact[0], contact[1]))
                
                
    except (Exception, Error) as error:
        print("ERROR:", error)
   



# partialname()
# deletedatabynumber()
# add_users()



cursor.close()
conn.close()
