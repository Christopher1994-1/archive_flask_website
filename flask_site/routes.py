import math
from flask import Flask, render_template, redirect, request, flash, url_for, send_from_directory
from flask_site.forms import AddingImages, RegistrationForm, LoginForm, AdminLogin, AddingPictures, SearchImages, AddAdmin, NavBarSearch
from flask_site import app
import os
from flask_login import login_user, current_user, logout_user, login_required
from flask_site import bcrypt, db, ALLOWED_EXTENSIONS, secure_filename
from flask_site.models import AdminInfo, Approval, Members, Images, Documents, Approval
from flask_paginate import Pagination, get_page_parameter, get_page_args
from werkzeug.security import generate_password_hash, check_password_hash
import smtplib

# functions *******************************************************

def approve_email(name, email):
    my_pass = os.environ.get('ggg')
    my_email = "cejvanniekirk098@gmail.com"
    message = f"""Hello {name}\n\nYou are getting this email because your application to join family archives has been approved. You can now login in with the email and password you have provided.\n\n
        if you wish to add data to these archives you can go to the site and navigate to the add data page and go through the application."""
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(my_email, my_pass)
        subject = 'Approved!'
        body = message

        msg = f"Subject: {subject}\n\n{body}"

        smtp.sendmail(my_email, email, msg)



def deny_email(name, email):
    my_pass = os.environ.get('ggg')
    my_email = "cejvanniekirk098@gmail.com"
    message = f"""Hello {name}\n\nYou are getting this email because your application to join family archives has been denied.
                \n\nPossible Reasons:\n\nInvaild Details:\n\nNot a family member:\n\n\nIf you are a family member try again or contact owner"""

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(my_email, my_pass)
        subject = 'Deined!'
        body = message

        msg = f"Subject: {subject}\n\n{body}"

        smtp.sendmail(my_email, email, msg)



def send_email(name, address, email, dob):
    my_pass = os.environ.get('ggg')
    my_email = "cejvanniekirk098@gmail.com"
    receiver = "kirko190255@gmail.com" # TODO change to os after restart
    message = f"""New user has been added and wants to be approved.\n\nUser Information:\n\n{name}\n\n{address}\n\n{email}\n\n{dob}\n\nPlease login to approve/deny this user."""

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(my_email, my_pass)
        subject = 'New User Sign Up!'
        body = message

        msg = f"Subject: {subject}\n\n{body}"

        smtp.sendmail(my_email, receiver, msg)


def user_await(name, email):
    name = name.split(' ')[0]
    my_pass = os.environ.get('ggg')
    my_email = "cejvanniekirk098@gmail.com"
    message = f"""Hey {name}\n\nYou are getting this email to let you know your information has been saved and is now awaiting approval."""

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(my_email, my_pass)
        subject = 'Awaiting Approval'
        body = message

        msg = f"Subject: {subject}\n\n{body}"

        smtp.sendmail(my_email, email, msg)



# website routes ***************************************************



# route to main index home page
@app.route('/', methods=["GET", "POST"])
def non_auth_index():
    logout_user()
    return render_template('non_auth_index.html')


# route for loged in user
@app.route("/index.html")
@login_required
def index():
    return render_template("index.html")


# route to search images page
@app.route('/search_images.html', methods=["POST", "GET"])
@login_required
def search_images():
    page = request.args.get('page', default=1, type=int)
    images = Images.query.paginate(per_page=9, page=page)
    form = SearchImages()
    data = Images.query
    if form.validate_on_submit():
        pass


    return render_template('search_images.html', form=form, images=images)


# route to search docs page : for docs db
@app.route('/search_docs.html', methods=["POST", "GET"])
@login_required
def search_docs():
    page = request.args.get('page', default=1, type=int)
    documents = Documents.query.paginate(per_page=9, page=page)
    form = SearchImages()
    data = Documents.query
    if form.validate_on_submit():
        pass


    return render_template('search_docs.html', form=form, documents=documents)


# route to input search docs page
@app.route('/search_docs_page.html', methods=["POST", "GET"])
def search_docs_page():
    form = SearchImages()
    searched_query = form.searched.data
    page = request.args.get('page', default=1, type=int)
    documents = Documents.query.filter_by(name=searched_query).paginate(per_page=9, page=page)

    return render_template('search_docs_page.html', searched_query=searched_query, documents=documents, form=form)



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




# route to admin override page
@app.route('/admin_override.html', methods=["POST", "GET"])
def admin_override():
    global user_in2
    user_in2 = None
    if current_user.is_authenticated:
        user_in2 = True
        return render_template(url_for('admin_update.html'))
    form = AdminLogin() # login admin form
    if form.validate_on_submit():
        user_email = form.email.data
        user = AdminInfo.query.filter(AdminInfo.admin_email==user_email).first()
        if user and bcrypt.check_password_hash(user.admin_password, form.first_password.data):
            login_user(user, remember=True)
            return render_template("admin_update.html")
        else:
            flash("Login Unsuccessful. Please check your email and password!")

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
            new_member = Approval(a_name=full_name, a_address=address, a_dob=dob, a_email=email, a_password=hashed_password)
            user = Approval.query.filter(Approval.a_email==email).first()
            if user != None:
                flash("Please use another email")
            
            else:
                flash("Your account is now awaiting approval:")
                db.session.add(new_member)
                db.session.commit()
                send_email(full_name, address, email, dob)
                user_await(full_name, email)
                return redirect(url_for('sign_upp_example'))
        return render_template('sign_upp_example.html', form=form)
            


# route for admin to add images
@app.route('/admin_add_images.html', methods=["POST", "GET"])
def admin_add_images():
    form = AddingPictures()
    image_name = form.name.data
    image_url = form.img_url.data
    image_description = form.description.data

    new_image = Images(name=image_name, url=image_url, description=image_description)
    new_doc = Documents(name=image_name, url=image_url, description=image_description)
    selected = request.form.get('checkbox')


    if form.validate_on_submit() and selected == "1":
        try:
            db.session.add(new_image)
            db.session.commit()
            flash("Image Added Succeesfully!")
            return redirect(url_for('admin_add_images'))
        except:
            flash("There was an error adding the image")

    elif form.validate_on_submit() and selected == "2":
        try:
            db.session.add(new_doc)
            db.session.commit()
            flash("Document Added Succeesfully!")
            return redirect(url_for('admin_add_images'))
        except:
            flash("There was an error adding the document")

    return render_template('admin_add_images.html', form=form)




# Test route *****
@app.route('/test.html', methods=["POST", "GET"])
def test():
    form = AddAdmin()
    if form.validate_on_submit():

            hashed_password = bcrypt.generate_password_hash(form.confirm_password.data)
            email = form.admin_email.data

            new_member = AdminInfo(admin_email=email, admin_password=hashed_password)

            db.session.add(new_member)
            db.session.commit()
    return render_template('test.html', form=form)



# image page search route : for images db
@app.route('/search', methods=["POST", "GET"])
def search():
    form = SearchImages()
    searched_query = form.searched.data
    page = request.args.get('page', default=1, type=int)
    images = Images.query.filter_by(name=searched_query).paginate(per_page=9, page=page)

    return render_template('search.html', searched_query=searched_query, images=images, form=form)


# route for user approval
@app.route('/user_approval.html', methods=["POST", "GET"])
def user_approval():
    page = request.args.get('page', default=1, type=int)
    users = Approval.query.paginate(per_page=5, page=page)

    return render_template('user_approval.html', users=users)



# route/function for admin to deny user
@app.route('/deny/<int:id>')
def deny(id):
    page = request.args.get('page', default=1, type=int)
    users = Approval.query.paginate(per_page=5, page=page)

    user_to_del = Approval.query.get_or_404(id)

    try:
        db.session.delete(user_to_del)
        db.session.commit()
        email = user_to_del.a_email
        name = user_to_del.a_name.split(' ')[0]

        deny_email(name, email)

        return redirect('/user_approval.html')
    except:
        flash('There was an error')

        return render_template('user_approval.html', users=users)


# # route/function for admin to approve user
@app.route('/approve/<int:id>')
def approve(id):
    page = request.args.get('page', default=1, type=int)
    users = Approval.query.paginate(per_page=5, page=page)

    user_to_approve = Approval.query.get_or_404(id)


    try:
        name = user_to_approve.a_name
        address = user_to_approve.a_address
        dob = user_to_approve.a_dob
        email = user_to_approve.a_email
        password = user_to_approve.a_password
        new_member = Members(name=name, address=address, DOB=dob, email=email, password=password)
        db.session.add(new_member)
        db.session.commit()
        
        dele = Approval.query.get_or_404(id)
        db.session.delete(dele)
        db.session.commit()
        approve_email(name.split(" ")[0], email)
        return redirect('/user_approval.html')
    except:
        pass

    return render_template("user_approval.html", users=users)


# search stuff **************************************


# search name route
@app.route('/search_name.html', methods=["GET", "POST"])
def search_name():
    user_input = None
    return render_template('search_name.html')





# family member page routes ***************************************

@app.route('/family_member_1.html')
def family_member_1():
    return render_template('family_member_1.html')