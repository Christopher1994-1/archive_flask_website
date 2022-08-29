from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


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

from flask_site import routes