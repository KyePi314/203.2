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

@main.route("/home/")
@login_required
def home():
    return render_template('home.html', username=current_user.UserName)

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

@main.route("/Timeline/")
def timeline():
    return render_template("Timeline.html")


@main.route("/userprofile/")
def userprofile():
    return render_template("userProfile.html", user=current_user.UserName, pwd=current_user.Password, email=current_user.Email, mana=current_user.Mana, awards=current_user.Awards, comments=current_user.Comments, posts=current_user.Posts, accountType=current_user.AccountType)

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


@main.route("/culture/")
def culture():
    return render_template("culture.html")

@main.route("/history/")
def history():
    return render_template("history.html")

@main.route("/species/")
def species():
    return render_template("species.html")

@main.route("/religion/")
def religion():
    return render_template("religion.html")

@main.route("/about/")
def about():
    return render_template("about.html")

@main.route("/specificDetails/")
def specificDetails():
    return render_template("specificDetails.html")

@main.route("/createworld/")
def createworld():
    return render_template("createworld.html")

app = create_app()


if __name__ == '__203.main__':
    app.run(debug=True)