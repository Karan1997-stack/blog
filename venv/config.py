import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    #'4c94bc8e484f68b7eb436e82940fe303'
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    #'sqlite:///site.db'
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    #'smtp.gmail.com'
    MAIL_PORT = os.environ.get('MAIL_PORT')
    #587
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    #True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    #'anothertale28@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    #'Itried123'
