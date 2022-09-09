from email.mime import image
import mimetypes
from flask import Flask, render_template, redirect, request, flash, url_for, send_from_directory
from flask_site.forms import AddingImages, RegistrationForm, LoginForm, AdminLogin
from flask_site import app
import os
from flask_login import login_user, current_user, logout_user, login_required
import mysql.connector
from flask_site import bcrypt, db, ALLOWED_EXTENSIONS, secure_filename
from flask_site.models import Members, Images
from flask_paginate import Pagination, get_page_parameter
from werkzeug.security import generate_password_hash, check_password_hash

# functions routes may need


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


# website routes

# route to main index home page
@app.route('/')
def non_auth_index():
    logout_user()
    return render_template('non_auth_index.html')


# route for loged in user
@app.route("/index.html")
@login_required
def index():
    return render_template("index.html")


# route to search images page
@app.route('/search_images.html')
@login_required
def search_images():
    pics = os.listdir('C:/Users/yklac/Desktop/projects/git_projects/flask_website/flask_site/static/images/search_images')
    return render_template('search_images.html', pics=pics)


# route to add data page
@app.route('/add_data.html')
@login_required
def add_data():
    return render_template('add_data.html')



# route to about page
@app.route('/about.html')
def about():
    return render_template('about.html')



# route to family tree page
@app.route('/family_tree.html')
@login_required
def family_tree():
    return render_template('family_tree.html')



# route to conditional sign up success page
@app.route('/sign_upp_success.html')
def sign_upp_success():
    return render_template('sign_upp_success.html')



# route to conditional sign up failure page
@app.route('/sign_upp_failed.html')
def sign_upp_failed():
    return render_template('sign_upp_failed.html')



# route to admin override page
@app.route('/admin_override.html', methods=["POST", "GET"])
def admin_override():
    form = AdminLogin()
    return render_template('admin_override.html', form=form)



# route to conditional admin update page
@app.route('/admin_update.html')
# @login_required
def admin_update():
    return render_template('admin_update.html')



# route for admin control - change admin information
@app.route('/admin_options/change_admin_info.html')
@login_required
def change_admin_info():
    return render_template('change_admin_info.html')


# route for users/family members to sign in
@app.route('/user_login.html', methods=["GET", "POST"])
def user_login():
    global user_in
    user_in = None
    if current_user.is_authenticated:
        user_in = True
        return render_template(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user_email = form.email.data
        user = Members.query.filter(Members.email==user_email).first()
        if user and bcrypt.check_password_hash(user.password, form.first_password.data):
            login_user(user, remember=form.remember.data)
            return render_template("index.html")
        else:
            flash("Login Unsuccessful. Please check your email and password!")
    return render_template("user_login.html", form=form, user_in=user_in)



# route for family members to sign up
@app.route('/sign_upp_example.html', methods=["GET", "POST"])
def sign_upp_example():
        form = RegistrationForm()
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.confirm_password.data)
            full_name = form.full_name.data
            address = form.address.data
            dob = form.dob.data
            email = form.form_email.data
            new_member = Members(name=full_name, address=address, DOB=dob, email=email, password=hashed_password)
            user = Members.query.filter(Members.email==email).first()
            if user != None:
                flash("Please use another email")
            
            else:
                db.session.add(new_member)
                db.session.commit()
                return redirect(url_for('sign_upp_success'))
        return render_template('sign_upp_example.html', form=form)
            

# route for admin to add images
@app.route('/admin_add_images.html', methods=["POST", "GET"])
def admin_add_images():
    form = AddingImages()
    # TODO add code to take image uploaded here and add it to the search_images folder, and have an option
    # to choose which folder you want to add too
    return render_template('admin_add_images.html', form=form)