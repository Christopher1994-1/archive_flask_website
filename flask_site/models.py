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

# error when trying to create.all() function
class Images(db.Model):
    __bind_key__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    path = db.Column(db.Text, nullable=True)
    description = db.Column(db.Text, nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return Members.query.get(int(user_id))

 