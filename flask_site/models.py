from flask_site import db, login_manager
from flask_login import UserMixin

# Create db model
class Members(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    DOB = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)


class Images(db.Model):
    __bind_key__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=False)



class Documents(db.Model):
    __bind_key__ = 'documents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=False)


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

@login_manager.user_loader
def load_user(user_id):
    return Members.query.get(int(user_id))

 