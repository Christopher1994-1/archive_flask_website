import mysql.connector
import os


# mysql_psw = os.environ.get('my_thing')

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     passwd=f"{mysql_psw}")

# conn = mydb.cursor()

# # conn.execute("CREATE DATABASE members")
# conn.execute("SELECT * FROM members.members;")
# result = conn.fetchall()
# results_list = []

# for row in result:
#     id, name, address, dob, email, hash_psw = row
#     results_list.append(email)
    

# print("No Errors")
# print()
# print(results_list)


email_to_pass = 'maik_po@gmail.com'


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
        return True
    else:
        return False


print(check_email(email_to_pass))

# TODO if works make it into a function that you can call and returns True or False