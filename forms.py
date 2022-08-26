from genericpath import exists
from xml.dom import ValidationErr
from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators
from wtforms.validators import DataRequired, Email, Length, EqualTo, email_validator, ValidationError
import email_validator
import mysql.connector
import os

# TODO look through db to see if something exists


# Class for user registration form
class RegistrationForm(FlaskForm):
    full_name = StringField("Full Name:", validators=[DataRequired()])
    dob = StringField("Date of Birth:", validators=[DataRequired()])
    address = StringField("Street Address", validators=[DataRequired()])
    email = StringField("Email", [validators.DataRequired(), validators.Email()])
    first_password = PasswordField("Password:", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('first_password')])
    register = SubmitField("Register")

    def validate_email(self, email):
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
    
        if email in results_list:
            exist = True
    
        if exist:
            raise ValidationError('That email already exists: please choose another')


# Class for user login form
class LoginForm(FlaskForm):
    email = StringField("Email", [validators.DataRequired(), validators.Email()])
    first_password = PasswordField("Password:", validators=[DataRequired(), Length(min=8)])
    register = SubmitField("Login")