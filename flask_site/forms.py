from genericpath import exists
from logging import PlaceHolder
from math import remainder
from xml.dom import ValidationErr
from xmlrpc.client import Boolean
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators, FileField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, EqualTo, email_validator, ValidationError
import email_validator
import mysql.connector
import os
from flask_site.models import Members, Images

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


# Class for adding images
class AddingImages(FlaskForm):
    image = FileField("Image File")
    submit = SubmitField("Upload")



# class for adding images to images db
class AddingPictures(FlaskForm):
    name = StringField('Image Name:', [validators.DataRequired()])
    img_url = StringField("Image URL:")
    description = TextAreaField("Add Description:")
    submit = SubmitField("Upload")


# class for images search
class SearchImages(FlaskForm):
    searched = StringField('Search', [validators.DataRequired()])
    submit = SubmitField('Submit')


# class for adding one admin user
class AddAdmin(FlaskForm):
    admin_email = StringField("Email", [validators.DataRequired(), validators.Email()])
    first_password = PasswordField("Password:", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('first_password')])
    register = SubmitField("Register")


# class for searching db names
class SearchForm(FlaskForm):
    input = StringField('Search', [validators.DataRequired()], render_kw={"placeholder": "Search"})
    submit = SubmitField('Submit')


# class for updating/adding family members
class FamilyForm(FlaskForm):
    first_name = StringField("First Name:", [validators.DataRequired()])
    last_name = StringField("Last Name:", [validators.DataRequired()])
    dob = StringField("Date of Birth:", [validators.DataRequired()])
    dod = StringField("Date of Death:", [validators.DataRequired()])
    pob = StringField("Place of Birth:", [validators.DataRequired()])
    pod = StringField("Place of Death:", [validators.DataRequired()])
    submit = SubmitField('Submit')