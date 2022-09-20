import mysql.connector
import os
import sqlite3
from flask_site.models import Images, Members 
from flask_sqlalchemy import SQLAlchemy
from flask_site import db



# data = Images.query
# ma = list(data)

# if "2" in ma:
#     print('True')
name = "John"
message = f"""Hello {name}\n\nYou are getting this email because your application to join family archives has been approved. You can now login in with the email and password you have provided.\n\n
if you wish to add data to these archives you can go to the site and navigate to the add data page and go through the application."""
print(message)
# mysql_pass = os.environ.get('my_thing')

# fun_db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         passwd=f"{mysql_pass}",
#     )

# my_cursor = fun_db.cursor()
# my_cursor.execute("CREATE DATABASE approval")
# # for i in my_cursor.execute("SELECT * FROM images.images WHERE images.name = ?", [search]):
# #     print(i)

# print("No Errors")


# db = sqlite3.connect("passwords.db")

# conn = db.cursor()


# conn.execute("INSERT INTO passwords VALUES ('Reddit', 'Kirk8829', 'Reddit0098Cuck')")

# for row in conn.execute("SELECT * FROM passwords"):
#     print(row)
