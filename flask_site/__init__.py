from cmath import log
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_image_search import ImageSearch
from werkzeug.utils import secure_filename


app = Flask(__name__)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'user_login'
UPLOAD_FOLDER = 'C:/Users/yklac/Desktop/projects/git_projects/flask_website/flask_site/static/images/search_images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# environment variables
mysql_psw = os.environ.get('my_thing')

# app config stuff
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://root:{mysql_psw}@localhost:3306/members'

app.config['SQLALCHEMY_BINDS'] = {
    'admin_info': f'mysql+pymysql://root:{mysql_psw}@localhost:3306/admin_info',
    'images' : f'mysql+pymysql://root:{mysql_psw}@localhost:3306/images'
}


app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# secret key for form
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# Initialize the database
db = SQLAlchemy(app)
image_search = ImageSearch(app, tensorflow=False)
from flask_site import routes