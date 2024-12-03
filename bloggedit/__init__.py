from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy as sqla
from flask_bcrypt import Bcrypt as bc
from flask_login import LoginManager
# from flask_mail import Mail

# from models import User, Post # using this only gives error as the whole module is interpreted when compiling

app = Flask(__name__)
# Set Secret Key to protect from cross-site request forgery, change cookies requests
app.config['SECRET_KEY'] = 'e08dd73152b14e7a0c2b7503412534ba'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' #  /// is the relative path from the current directory

# Database Instance
db = sqla(app)
# Bcrypt Instance
bcrypt = bc(app)
# Login Manager Instance
login_manager = LoginManager(app)
# Login Manager Settings
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
# app.config['MAIL_SERVER'] = 'outlook.office365.com'
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
# app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
# mail = Mail(app)

from bloggedit import routes