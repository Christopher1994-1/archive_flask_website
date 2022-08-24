# import sqlite3

# db = sqlite3.connect('passwords.db')

# conn = db.cursor()

# conn.execute("CREATE TABLE admin_info ('username TEXT', 'password TEXT', 'email TEXT')")

# conn.execute("INSERT INTO admin_info VALUES ('example_user', 'example_psw', 'example@example.com')")


# for row in conn.execute("SELECT * FROM passwords"):
#     print(row)

import mysql.connector
import os

# mysql_psw = os.environ.get('my_thing')
# myNum = os.environ.get('my_number')

# print()
# print(type(mysql_psw))
# print()
# print(mysql_psw)

# print("=" * 40)

# print()
# print(type(myNum))
# print()
# print(myNum)

mysql_psw = os.environ.get('my_thing')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=f"{mysql_psw}",)

conn = mydb.cursor()

# conn.execute("CREATE DATABASE members")
