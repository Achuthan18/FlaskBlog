from flask_wtf import FlaskForm 
from wtforms import StringField,PasswordField,SubmitField,BooleanField,Form
from wtforms.validators import email,DataRequired,length,EqualTo,Email,ValidationError
from blog.models import User,Post

class RegistrationForm(FlaskForm):

    username=StringField('Username',validators=[DataRequired(),length(min=2,max=14)])

    email=StringField('Email',validators=[DataRequired(),Email()])

    password=PasswordField('Password',validators=[DataRequired()])

    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])

    submit=SubmitField('Sign Up')

    def validate_username(self,username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is taken! Please try another Username')
        
    def validate_email(self,email):
        user=User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(f'An account already exists for {email.data}')    

class LoginForm(FlaskForm):

    email=StringField('Email',validators=[DataRequired(),email()])

    password=PasswordField('Password',validators=[DataRequired()])

    remember=BooleanField('Remember Me')
    
    submit=SubmitField('Login')    

