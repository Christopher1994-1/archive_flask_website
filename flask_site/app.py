from email import message
from urllib import request
from wsgiref.validate import validator
from flask import Flask, render_template, redirect, request, flash, url_for 
from flask_sqlalchemy import SQLAlchemy
import os
import mysql.connector
from flask_bcrypt import Bcrypt
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from forms import RegistrationForm, LoginForm, AdminLogin
from flask_login import LoginManager, UserMixin


app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


# environment variables
mysql_psw = os.environ.get('my_thing')




# app config stuff
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{mysql_psw}@localhost:3306/members'
app.config['SQLALCHEMY_BINDS'] = {
    'admin_info': f'mysql+pymysql://root:{mysql_psw}@localhost:3306/admin_info',
}

# secret key for form
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY



# Initialize the database
db = SQLAlchemy(app)

# Create db model
class Members(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    DOB = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return Members.query.get(int(user_id))


# TODO finish admin_override route db stuff
# TODO add email and password checks for admin login form
# TODO see if @login_manager can have two sepate things, one for users and one for admin

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


if __name__ == "__main__":
    app.run(debug=True)
