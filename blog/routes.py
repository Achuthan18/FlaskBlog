
from flask import render_template,url_for,flash,redirect,request
from blog import app,db,bcrypt
from blog.models import User,Post
from blog.forms import RegistrationForm,LoginForm
from flask_login import login_user,current_user


posts=[
    { 'author':'Achuthan','content':'football','title':'first blog post','date_posted':'April 10th 2023'
    },
    {
        'author':'ABDULLA AKMAL KANNAN',
        'title':'kannante kunnatharam',
        'content':'kunnatharam',
        'title':'The Art Of Kunatharam ',
        'date_posted':'June 2nd 2023'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('Home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('About.html',title='about')

@app.route("/register",methods=['GET','POST'])
def register():
    
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form=RegistrationForm()
    if request.method=='POST'and form.validate():
     hashed_pw=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
     user=User(username=form.username.data,email=form.email.data,password=hashed_pw)
     db.session.add(user)
     db.session.commit()
     flash(f"Account created for {form.username.data} You can now log in !",'success')
     return redirect(url_for('login'))
    else:
        print(form.errors)
    return render_template('Register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST']) 
def login():

    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form=LoginForm() 
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            return redirect(url_for('home'))
          
        else:
            flash("Login Unsuccesful! Please Check email and password")
    return render_template('Login.html',title='Login',form=form) 