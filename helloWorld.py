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

        # """CREATE TABLE product ( `id` INT NOT NULL AUTO_INCREMENT , `name` VARCHAR(127) NOT NULL , `price` DOUBLE NOT NULL , `stock` INT NOT NULL , PRIMARY KEY (`id`))"""
        # """INSERT INTO users (username, password) VALUES ('LuminaT', 'gigapass')"""

    '''
    sql_select_Query = "SELECT * FROM users"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in users is: ", cursor.rowcount)

    print("\nPrinting each user record")
    for row in records:
        print("######################################")
        print("id = ", row[0], )
        print("username = ", row[1])
        print("password  = ", row[2])
        print("date created  = ", row[3])
        print("######################################\n")
    '''

    # query = ;

    # result = cursor.execute(query);
    # connection.commit()

    # print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
