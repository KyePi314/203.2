### IMPORTING PACKAGES ###
from flask import Flask, render_template, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, current_user, LoginManager
from flask_login import UserMixin
from __init__ import create_app
import base64

main = Blueprint('main', __name__)


@main.route("/", methods=['POST', 'GET'])
def index():
    return render_template("auth/login.html")

@main.get('/home/')
@login_required
def home():
    from models import session, Post, Comment
    find_post = session.query(Post).all()
    find_comment = session.query(Comment).all()
    return render_template("home.html", posts=find_post, username=current_user.UserName, comments=find_comment)

@main.route("/contact/")
def contact():
    return render_template("Contact.html")

@main.route("/Issues/")
def issues():
    return render_template("Issues.html")

@main.route("/Maps/")
def maps():
    return render_template("Maps.html")



@main.route("/subscription/")
def subscription():
    return render_template("SubscriptionPage.html")

@main.route("/userprofile/")
def userprofile():
    return render_template("userprofile.html", user=current_user.UserName, pwd=current_user.Password, email=current_user.Email, mana=current_user.Mana, awards=current_user.Awards, comments=current_user.Comments, posts=current_user.Posts, accountType=current_user.AccountType)

@main.route("/images/")
def images():
    from models import session, Img
    imgs = session.query(Img).filter_by(UserName = current_user.UserName).all()
    img_list = []
    # read image data from db back to form a rendable in html
    for img in imgs:
        image = base64.b64encode(img.data).decode('ascii')
        img_list.append(image)
    return render_template("images.html", img_list = img_list )

@main.route("/about/")
def about():
    return render_template("about.html")

@main.route("/createworld/")
def createworld():
    return render_template("createworld.html")

app = create_app()


if __name__ == '__203.main__':
    app.run(debug=True)