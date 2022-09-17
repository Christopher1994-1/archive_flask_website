import mysql.connector
import os
import sqlite3
from flask_site.models import Images, Members 
from flask_sqlalchemy import SQLAlchemy
from flask_site import db



data = Images.query
ma = list(data)

if "2" in ma:
    print('True')

# mysql_pass = os.environ.get('my_thing')

# fun_db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         passwd=f"{mysql_pass}",
#         database="images"
#     )

# my_cursor = fun_db.cursor()
# # my_cursor.execute("CREATE DATABASE images")
# for i in my_cursor.execute("SELECT * FROM images.images WHERE images.name = ?", [search]):
#     print(i)

# print("No Errors")


# db = sqlite3.connect("passwords.db")

# conn = db.cursor()


# conn.execute("INSERT INTO passwords VALUES ('Ancestry', 'Kirko Email', 'Ancestry0098@')")

# for row in conn.execute("SELECT * FROM passwords"):
#     print(row)
