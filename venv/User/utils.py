import os,secrets
import secrets
from PIL import Image
from flask import url_for
from flask_mail import Message
from venv import mail
from flask import current_app



def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _,fext= os.path.splitext(form_picture.filename)
    picture_fn = random_hex + fext
    picture_path = os.path.join(current_app.root_path, 'static\profile_pics', picture_fn)
    #print(picture_path)
    #form_picture.save(picture_path)

    output_size= (125,125)
    i=Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

def save_theme(form_picture):
    random_hex = secrets.token_hex(8)
    _,fext= os.path.splitext(form_picture.filename)
    picture_fn = random_hex + fext
    picture_path = os.path.join(current_app.root_path, 'static\post_pics', picture_fn)
    #print(picture_path)
    #form_picture.save(picture_path)

    output_size= (700,300)
    i=Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',sender='noreply@demo.com',recipients=[user.email])
    msg.body= f'''
    To reset your password, visit the following link: {url_for('users.reset_token',token=token,_external=True)}
    If you did not make thie request, Ignore this mail and no changes will take effect.
    '''
    mail.send(msg)
