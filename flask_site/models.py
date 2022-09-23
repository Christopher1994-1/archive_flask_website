from flask_site import db, login_manager
from flask_login import UserMixin

# Create db model for members
class Members(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    DOB = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)


# DB for images and urls for images
class Images(db.Model):
    __bind_key__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=False)


# DB for documents and urls for documents
class Documents(db.Model):
    __bind_key__ = 'documents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=False)


# DB for memebers info to be stored before being approved
class Approval(db.Model):
    __bind_key__ = 'approval'
    id = db.Column(db.Integer, primary_key=True)
    a_name = db.Column(db.String(200), nullable=False)
    a_address = db.Column(db.String(200), nullable=False)
    a_dob = db.Column(db.String(50), nullable=False)
    a_email = db.Column(db.String(200), nullable=False)
    a_password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Approval('{self.id}', '{self.a_name}', '{self.a_address}', '{self.a_dob}', '{self.a_email}', '{self.a_password}')" 


# DB for admin login information
class AdminInfo(db.Model, UserMixin):
    __bind_key__ = 'admin_info'
    id = db.Column(db.Integer, primary_key=True)
    admin_email = db.Column(db.String(200), nullable=False)
    admin_password = db.Column(db.String(200), nullable=False)


# DB for family members and all their information
class FamilyMembers(db.Model):
    __bind_key__ = 'family_members'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    dob = db.Column(db.String(50), nullable=False) # dob = date of birth
    dod = db.Column(db.String(50), nullable=True)  # dod = date of death
    pob = db.Column(db.String(50), nullable=False) # pob = place of birth
    pod = db.Column(db.String(50), nullable=True)  # pod = place of death


    def __repr__(self):
        return f"('{self.id}', '{self.first_name}',  '{self.last_name}', '{self.dob}', '{self.dod}', '{self.pob}', '{self.pod}')"


# TODO think of other possible columns for db 
# TODO add search bar into search_name.html
# TODO add functionality to search bar in narbar that when searched searches names also images.
# TODO after confident no more columns create db and test search for results
# TODO make a way so that logged in users cannot see sign up button


@login_manager.user_loader
def load_user(user_id):
    return Members.query.get(int(user_id))

 