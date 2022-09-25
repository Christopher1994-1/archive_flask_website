import mysql.connector
import os
import sqlite3
from flask_site.models import Images, Members, FamilyMembers
from flask_sqlalchemy import SQLAlchemy
from flask_site import db

searched_data = "doe"

user = FamilyMembers.query.filter(FamilyMembers.first_name==searched_data).first()

users = FamilyMembers.query.filter(FamilyMembers.last_name==searched_data).all()
pick = []

if user:
    user=user
    urls = user.first_name + "_" + user.last_name 
    new_url = urls.lower()
    print(new_url)
elif users:
    users=users
    for user in users:
        user = user.first_name + "_" + user.last_name
        pick.append(user.lower())
    print(pick)


# data = Images.query
# ma = list(data)

# if "2" in ma:
#     print('True')

# mysql_pass = os.environ.get('my_thing')

# fun_db = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         passwd=f"{mysql_pass}",
#     )

# my_cursor = fun_db.cursor()
# my_cursor.execute("CREATE DATABASE family_members")
# # for i in my_cursor.execute("SELECT * FROM images.images WHERE images.name = ?", [search]):
# #     print(i)

# print("No Errors")


# db = sqlite3.connect("passwords.db")

# conn = db.cursor()


# conn.execute("INSERT INTO passwords VALUES ('Discord', 'Kirko', 'FuckDiscord098')")

# for row in conn.execute("SELECT * FROM passwords"):
#     print(row)
