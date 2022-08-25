import mysql.connector
import os



mysql_psw = os.environ.get('my_thing')

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=f"{mysql_psw}",
    database="members")

conn = mydb.cursor()

# conn.execute("CREATE DATABASE members")

print("No Errors")
