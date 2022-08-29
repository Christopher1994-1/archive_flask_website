import imp
from flask import Flask, render_template, redirect, request, flash, url_for 
from flask_site.forms import RegistrationForm, LoginForm, AdminLogin
from flask_site import app
import os
import mysql.connector
from flask_site import bcrypt, db
from flask_site.models import Members
from werkzeug.security import generate_password_hash, check_password_hash

# website routes

# route to main index home page
@app.route('/')
def index():
    return render_template('non_auth_index.html')



# route to search images page
@app.route('/search_images.html')
def search_images():
    return render_template('search_images.html')



# route to add data page
@app.route('/add_data.html')
def add_data():
    return render_template('add_data.html')



# route to about page
@app.route('/about.html')
def about():
    return render_template('about.html')



# route to family tree page
@app.route('/family_tree.html')
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

    sql_psw = os.environ.get('my_thing')
    fun_db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=f"{sql_psw}"
    )
    return render_template('admin_override.html', form=form)



# route to conditional admin update page
@app.route('/admin_update.html')
def admin_update():
    return render_template('admin_update.html')



# route for admin control - change admin information
@app.route('/admin_options/change_admin_info.html')
def change_admin_info():
    return render_template('change_admin_info.html')



# route for non-signed in user:
@app.route('/non_auth_index.html')
def non_auth_index():
    return render_template('non_auth_index.html')


# route for users/family members to sign in
@app.route('/user_login.html', methods=["GET", "POST"])
def user_login():
    # TODO add user login info
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('user_login.html', form=form)



# route for family members to sign up
@app.route('/sign_upp_example.html', methods=["GET", "POST"])
def sign_upp_example():
        form = RegistrationForm()
        if form.validate_on_submit():
            if request.method == "POST":
                full_name = request.form['full_name']
                address = request.form['address']
                date_birth = request.form['dob']
                email = request.form['form_email']
                password = request.form['confirm_password']
                hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
                new_member = Members(name=full_name, address=address, DOB=date_birth, password=hashed_password, email=email)

        # Pushing to db
                try:
                    db.session.add(new_member)
                    db.session.commit()
                    return render_template('sign_upp_success.html')
                except:
                    return render_template('sign_upp_failed.html')
                else:
                    return redirect(url_for('sign_upp_success'))

        return render_template('sign_upp_example.html', form=form)
