from unicodedata import name
import mysql.connector
import os




mysql_pass = os.environ.get('my_thing')

fun_db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=f"{mysql_pass}"
    )

my_cursor = fun_db.cursor()
my_cursor.execute("CREATE DATABASE images")

print("No Errors")
