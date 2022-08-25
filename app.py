# from crypt import methods
from email import message
from urllib import request
from wsgiref.validate import validator
from flask import Flask, render_template, redirect, request, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField, validators
from wtforms.validators import DataRequired, EqualTo, Length, InputRequired
from forms import RegistrationForm, LoginForm

app = Flask(__name__)


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



# create register form class
class RegisterForm(FlaskForm):
    full_name = StringField("Full Name:", validators=[InputRequired()])
    address = StringField("Address:", validators=[DataRequired()])
    DOB = StringField("Date Of Birth:", validators=[DataRequired()])
    email = StringField("Email:", validators=[DataRequired()])
    password_hash = PasswordField("Password:", validators=[DataRequired(), validators.EqualTo('password_confirm', message="Passwords Must Match")])
    password_confirm = PasswordField("Confirm Password:")
    register = SubmitField("Register")



# TODO watch youtube video on adding names to form calls for html form things



# Initialize the database
db = SQLAlchemy(app)

# Create db model
class Members(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    DOB = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    # adding password hash
    password_hash = db.Column(db.String(200), nullable=False)


    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute!")
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Create a method to return a string when we add something
    # def __repr__(self):
    #     return '<Name %r>' % self.id





# create db model for admin info database
class Admin_info(db.Model):
    __bind_key__ = 'admin_info'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(200), nullable=False)



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



# route to sign up page/ delete-----
@app.route('/sign_upp.html', methods=["POST", "GET"])
def sign_upp():

    if request.method == "POST":
        full_name = request.form['full_name']
        address = request.form['address']
        date_birth = request.form['dob']
        email = request.form['email']
        password = request.form['psw']
        new_member = Members(name=full_name, address=address, DOB=date_birth, password=password, email=email)

        # Pushing to db
        try:
            db.session.add(new_member)
            db.session.commit()
            return render_template('sign_upp_success.html')
        except:
            return render_template('sign_upp_failed.html')
    else:
        return render_template('sign_upp.html')



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
@app.route('/admin_override.html')
def admin_override():
    sql_psw = os.environ.get('my_thing')
    

    admin_username = None
    admin_psw = None
    return render_template('admin_override.html')



# route to conditional admin update page
@app.route('/admin_update.html')
def admin_update():
    return render_template('admin_update.html')



# route for admin control - change admin information
@app.route('/admin_options/change_admin_info.html')
def change_admin_info():
    return render_template('change_admin_info.html')



# route for admin set up, temp

# @app.route('/admin_setup.html', methods=["POST", "GET"])
# def admin_setup():
#     if request.method == "POST":
#         username = request.form['admin_full_name']
#         email = request.form['admin_email']
#         password = request.form['admin_psw']
#         new_member = Admin_info(username=username, password=password, email=email)

#         # Pushing to db
#         try:
#             db.session.add(new_member)
#             db.session.commit()
#             return render_template('sign_upp_success.html')
#         except:
#             return render_template('sign_upp_failed.html')
#     else:
#         return render_template('admin_setup.html')


# route for non-signed in user:
@app.route('/non_auth_index.html')
def non_auth_index():
    return render_template('non_auth_index.html')


# route for users/family members to sign in
@app.route('/user_login.html')
def user_login():
    return render_template('user_login.html')


@app.route('/sign_upp_example.html', methods=["GET", "POST"])
def sign_upp_example():
        form = RegistrationForm()
        if form.validate_on_submit():
            return redirect(url_for('sign_upp_success'))

        return render_template('sign_upp_example.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
