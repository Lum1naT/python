# Imports

import mysql.connector
from mysql.connector import Error


# Rowcount

cursor.rowcount

# Fetch

record = cursor.fetchall()

rows = cursor.fetchmany(size=1)

row = cursor.fetchone()



# Creating a connection

connection = mysql.connector.connect(host='localhost',
                                     database='db',
                                     user='root',
                                     password='')


# Checking if connection is valid

if connection.is_connected():

# Getting Database info

connection.get_server_info()



# Creating a cursor

cursor = connection.cursor()

# INSERT query

mySql_insert_query = """INSERT INTO table_name (Name, Price, Purchase_date)
                           VALUES
                           ('Lenovo ThinkPad P71', 6459, '2019-08-14') """
cursor.execute(mySql_insert_query)
connection.commit()

# INSERT query with bound variables

mySql_insert_query = """INSERT INTO table_name (Name, Price, Purchase_date)
                                VALUES (%s, %s, %s) """

        recordTuple = (name, price, purchase_date) #set the fucking variables man!
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()

# SELECT query with bound variables

 # cursor = connection.cursor(buffered=True)

sql_select_query = """SELECT * FROM table_name WHERE id = %s"""
id = 6
cursor.execute(sql_select_query, (id,))
record = cursor.fetchall()

for row in record:
    print("id = ", row[0], )
    print("Name = ", row[1])
    print("Join Date = ", row[2])
    print("Salary  = ", row[3], "\n")


# DELETE query with bound variables

sql_Delete_query = """DELETE FROM table_name WHERE id = %s"""
id = 6
cursor.execute(sql_Delete_query, (id,))
connection.commit()
print("Record Deleted successfully ")


# UPDATE single row

sql_update_query = """UPDATE table_name SET price = %s WHERE id = %s"""
        inputData = (price, id)
        cursor.execute(sql_update_query, inputData)
        connection.commit()
        print("Record Updated successfully")

# UPDATE multiple rows with a single query

sql_update_query = """UPDATE table_name SET Price = %s WHERE id = %s"""

records_to_update = [(3000, 3), (2750, 4)] #(price, id)
cursor.executemany(sql_update_query, records_to_update)
connection.commit()

print(cursor.rowcount, "Records of a laptop table updated successfully")



# DONT FROGET TO CLOSE cursor -> connection

cursor.close()

connection.close()





# BASE #

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='pythondb',
                                         user='root',
                                         password='')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
