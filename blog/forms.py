from flask_wtf import FlaskForm 
from wtforms import StringField,PasswordField,SubmitField,BooleanField,Form
from wtforms.validators import email,DataRequired,length,EqualTo,Email

class RegistrationForm(FlaskForm):

    username=StringField('Username',validators=[DataRequired(),length(min=2,max=14)])

    email=StringField('Email',validators=[DataRequired(),Email()])

    password=PasswordField('Password',validators=[DataRequired()])

    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])

    submit=SubmitField('Sign Up')

class LoginForm(FlaskForm):

    email=StringField('Email',validators=[DataRequired(),email()])

    password=PasswordField('Password',validators=[DataRequired()])

    remember=BooleanField('Remember Me')
    
    submit=SubmitField('Login')    
