import mysql.connector
import os

# TODO learn to quary the data inside db and try to learn to check if a value already exists

mysql_psw = os.environ.get('my_thing')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=f"{mysql_psw}",
    database="members")

conn = mydb.cursor()

# conn.execute("CREATE DATABASE members")

print("No Errors")
