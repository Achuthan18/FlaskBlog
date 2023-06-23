
from flask import render_template,url_for,flash,redirect,request
from blog import app
from blog.models import User,Post
from blog.forms import RegistrationForm,LoginForm


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
    form=RegistrationForm()
    if request.method=='POST'and form.validate():
     print("validated")
     flash(f"Account created for {form.username.data} !",'success')
     return redirect(url_for('home'))
    else:
        print(form.errors)
    return render_template('Register.html',title='Register',form=form)

@app.route("/login",methods=['GET','POST']) 
def login():
    form=LoginForm() 
    if form.validate_on_submit():
        if form.email.data=='admin@blog.com' and form.password.data=="password":
            flash("You have been logged in",'sucess')
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccesful! Please Check username and password")
    return render_template('Login.html',title='Login',form=form) 