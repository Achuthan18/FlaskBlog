from flask_wtf import FlaskForm 
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import email,DataRequired,length,EqualTo

class RegistrationForm(FlaskForm):

    username=StringField('Username',validators=[DataRequired(),length(min=2,max=14)])

    email=StringField('Email',validators=[DataRequired(),email()])

    Password=PasswordField('Password',validators=[DataRequired()])

    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo(Password)])

    submit=SubmitField('Sign Up')

class LoginForm(FlaskForm):

    email=StringField('Email',validators=[DataRequired(),email()])

    Password=PasswordField('Password',validators=[DataRequired()])

    remember=BooleanField('Remember Me')
    
    submit=SubmitField('Login')    

