from unicodedata import name
import mysql.connector
import os




# function to check email
def check_email(user_email):
    mysql_pass = os.environ.get('my_thing')

    fun_db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=f"{mysql_pass}"
    )

    my_cursor = fun_db.cursor()
    my_cursor.execute("SELECT * FROM members.members;")
    result = my_cursor.fetchall()
    results_list = []

    for row in result:
        id, name, address, dob, email, hash_psw = row
        results_list.append(email)
    
    if user_email in results_list:
        raise ValueError("Thing exists")
    else:
        print("Thing does't exist")


user_email = input("> ")
check_email(user_email)


# TODO if works make it into a function that you can call and returns True or False
