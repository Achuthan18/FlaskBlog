
import os
import secrets
from PIL import Image
from flask import render_template,url_for,flash,redirect,request
from blog import app,db,bcrypt
from blog.models import User,Post
from blog.forms import RegistrationForm,LoginForm,UpdateAccountForm
from flask_login import login_user,current_user,logout_user,login_required


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
            next_page=request.args.get('next')
            return redirect(url_for(next_page)) if next_page else redirect(url_for('home'))
          
        else:
            flash("Login Unsuccesful! Please Check email and password")

    return render_template('Login.html',title='Login',form=form)

 
@app.route("/logout") 
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    random_hex=secrets.token_hex(8)
    _,form_ext=os.path.splitext(form_picture.filename)
    picture_fn=random_hex+form_ext
    picture_path=os.path.join(app.root_path,'static/profile_pic',picture_fn)
    
    output_size=(128,128)
    i=Image.open(form_picture)
    i.thumbnail(output_size,Image.ANTIALIAS)

    prev_picture = os.path.join(app.root_path, 'static/profile_pic', current_user.image_file)
    if os.path.exists(prev_picture):
        os.remove(prev_picture)

    quality_val=90
    i.save(picture_path,quality=quality_val)

    return picture_fn


@app.route("/Account",methods=['GET','POST'])
@login_required
def account():
    form=UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file=save_picture(form.picture.data)
            current_user.image_file=picture_file
        current_user.username=form.username.data
        current_user.email=form.email.data
        db.session.commit()
        
        flash('your account info has been updated','success')
        return redirect(url_for("account"))
    elif request.method =='GET':
        form.username.data=current_user.username
        form.email.data=current_user.email
    image_file=url_for('static',filename='profile_pic/'+ current_user.image_file)
    return render_template('Account.html',title='Account',image_file=image_file,form=form)
