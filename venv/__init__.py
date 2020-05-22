from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from venv.config import Config

#app.config['SECRET_KEY']='4c94bc8e484f68b7eb436e82940fe303'
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
'''app.config['MAIL_SERVER']= 'smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']= True
app.config['MAIL_USERNAME']='anothertale28@gmail.com'
app.config['MAIL_PASSWORD']='Itried123'''

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    print('ok')

    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from venv.User.routes import users
    from venv.Post.routes import posts
    from venv.Main.routes import main
    from venv.Errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)
    return app


