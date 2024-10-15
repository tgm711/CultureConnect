import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_moment import Moment
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sk_test_51KITmdSCRVzSo3UYdIc7sDYWpDwKoPzsnXdtQsKQ9QvVypwinQd5oaZGNt2wV84kT9bfasJuZHGDDNuGweSmqrNr00lemkOJB1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/ruchi/OneDrive/Desktop/EcommerceWebsite-master - Copy/site1.db'
moment = Moment(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

from ecommerceweb import routes