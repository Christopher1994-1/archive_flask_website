from genericpath import exists
from math import remainder
from xml.dom import ValidationErr
from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators
from wtforms.validators import DataRequired, Email, Length, EqualTo, email_validator, ValidationError
import email_validator
import mysql.connector
import os
from flask_site.models import Members

# TODO look through db to see if something exists


# Class for user registration form
class RegistrationForm(FlaskForm):
    full_name = StringField("Full Name:", validators=[DataRequired()])
    dob = StringField("Date of Birth:", validators=[DataRequired()])
    address = StringField("Street Address", validators=[DataRequired()])
    form_email = StringField("Email", [validators.DataRequired(), validators.Email()])
    first_password = PasswordField("Password:", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('first_password')])
    register = SubmitField("Register")

# Class for user login form
class LoginForm(FlaskForm):
    email = StringField("Email", [validators.DataRequired(), validators.Email()])
    first_password = PasswordField("Password:", validators=[DataRequired(), Length(min=8)])
    remember = BooleanField("Remember Me")
    register = SubmitField("Login")



# Class for admin user login
class AdminLogin(FlaskForm):
    email = StringField("Email", [validators.DataRequired(), validators.Email()])
    first_password = PasswordField("Password:", validators=[DataRequired(), Length(min=8)])
    register = SubmitField("Login")
