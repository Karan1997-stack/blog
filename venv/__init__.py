from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
import os

app=Flask(__name__)
print('ok')

app.config['SECRET_KEY']='4c94bc8e484f68b7eb436e82940fe303'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt =Bcrypt(app)
login_manager= LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category='info'
app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']= True
app.config['MAIL_USERNAME']='anothertale28@gmail.com'
app.config['MAIL_PASSWORD']='Itried123'
mail = Mail(app)






from venv import route