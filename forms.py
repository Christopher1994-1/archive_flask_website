from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators
from wtforms.validators import DataRequired, Email, Length, EqualTo, email_validator
import email_validator


# Class for user registration form
class RegistrationForm(FlaskForm):
    full_name = StringField("Full Name:", validators=[DataRequired()])
    dob = StringField("Date of Birth:", validators=[DataRequired()])
    address = StringField("Street Address", validators=[DataRequired()])
    email = StringField("Email", [validators.DataRequired(), validators.Email()])
    first_password = PasswordField("Password:", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('first_password')])
    register = SubmitField("Register")


# Class for user login form
class LoginForm(FlaskForm):
    email = StringField("Email", [validators.DataRequired(), validators.Email()])
    first_password = PasswordField("Password:", validators=[DataRequired(), Length(min=8)])
    remember_me = BooleanField("Remember Me")
    register = SubmitField("Login")