from flask import Flask,render_template,url_for
from forms import RegistrationForm,LoginForm

app = Flask(__name__)
app.config['SECRET_KEY']='cbdb6e657cf758ceb5b343174751f5b75c1b'

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

@app.route("/register")
def register():
    form=RegistrationForm()
    return render_template('Register.html',title='Register',form=form)

@app.route("/login") 
def login():
    form=LoginForm()  
    return render_template('Login.html',title='Login',form=form) 

if __name__=='__main__':
    app.run(debug=True)