
from flask import render_template, request, Blueprint
from blog.models import Post

main=Blueprint('main',__name__)


@main.route("/")
@main.route("/home")
def home():
    page=request.args.get('page',1,type=int) #default value of page is 1
    posts=Post.query.order_by(Post.date_posted.desc()).paginate(page=page,per_page=3)
    return render_template('Home.html',posts=posts)

@main.route("/about")
def about():
    return render_template('About.html',title='about')