from unicodedata import name
import mysql.connector
import os
import sqlite3
from flask_site.models import Images, Members
from flask_sqlalchemy import SQLAlchemy

images = Images.query.all()

for image in images:
    print(image.url)


print()

m = Members.query.all()
for ma in m:
    print(ma)

# mysql_pass = os.environ.get('my_thing')

# fun_db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         passwd=f"{mysql_pass}",
#         database="images"
#     )

# my_cursor = fun_db.cursor()
# # my_cursor.execute("CREATE DATABASE images")
# for i in my_cursor.execute("SELECT * FROM images.images;"):
#     print(i)

# print("No Errors")


# db = sqlite3.connect("passwords.db")

# conn = db.cursor()


# conn.execute("INSERT INTO passwords VALUES ('Ancestry', 'Kirko Email', 'Ancestry0098@')")

# for row in conn.execute("SELECT * FROM passwords"):
#     print(row)
