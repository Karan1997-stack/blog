from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import User



class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=25)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    Submit=SubmitField('Register')

    def validate_username(self, uname) :
        u1 = User.query.filter_by(username=uname.data).first()
        if u1:
            raise ValidationError('That username is taken.Please choose another one!')

    def validate_email(self, ema) :
        u1= User.query.filter_by(email=ema.data).first()
        if u1:
            raise ValidationError('That Email is taken.Please choose another one!')

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=8)])
    remember = BooleanField('Remember Me')
    Submit=SubmitField('Sign In')



class UpdateAccountForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=25)])
    email=StringField('Email',validators=[DataRequired(),Email()])
    picture=FileField("Update Profile Picture", validators=[FileAllowed(['jpg','png'])])
    Submit=SubmitField('Update')

    def validate_username(self, uname) :
        if uname.data != current_user.username:
            u1 = User.query.filter_by(username=uname.data).first()
            if u1:
                raise ValidationError('That username is taken.Please choose another one!')

    def validate_email(self, ema) :
        if ema.data != current_user.email:
            u1= User.query.filter_by(email=ema.data).first()
            if u1:
                raise ValidationError('That Email is taken.Please choose another one!')


class PostForm(FlaskForm):
    title= StringField('Title',validators=[DataRequired()])
    content=TextAreaField('Content', validators=[DataRequired()])
    theme = FileField("Upload a theme for Post", validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField("Post!")

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')
    def validate_email(self, email) :
        u1 = User.query.filter_by(email=email.data).first()
        if u1 is None:
            raise ValidationError('There is no account with that email.')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

