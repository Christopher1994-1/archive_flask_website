from unicodedata import name
import mysql.connector
import os
import sqlite3
from Google import Create_Service

# path = 'C:/Users/yklac/Desktop/projects/git_projects/flask_website/flask_site/static/images/search_images'
# ma = os.listdir(path)
# print(ma)

# for filename in ma:
#     print(os.path.splitext(filename)[0])


# APP_ROOT = os.path.dirname(os.path.abspath(__file__))
# print(APP_ROOT)

# my = os.path.dirname(os.path.abspath(__file__))
# print("this is what it prints" + my)

# mysql_pass = os.environ.get('my_thing')

# fun_db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         passwd=f"{mysql_pass}"
#     )

# my_cursor = fun_db.cursor()
# my_cursor.execute("CREATE DATABASE images")

# print("No Errors")


# db = sqlite3.connect("passwords.db")

# conn = db.cursor()


# conn.execute("INSERT INTO passwords VALUES ('Ancestry', 'Kirko Email', 'Ancestry0098@')")

# for row in conn.execute("SELECT * FROM passwords"):
#     print(row)
