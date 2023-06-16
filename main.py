### IMPORTING PACKAGES ###
from flask import Flask, render_template, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, current_user, LoginManager
from flask_login import UserMixin
from __init__ import create_app



main = Blueprint('main', __name__)
detail = ""

@main.route("/")
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
   
@main.route("/worldsPage/")
def worlds():
    return render_template("worldsPage.html")

@main.route("/worldinfo/")
def worldinfo():
    return render_template("worldinfo.html", WorldName = "Placeholder")

@main.route("/userprofile/")
def userprofile():
    return render_template("userProfile.html", mana=current_user.Mana, awards=current_user.Awards, comments=current_user.Comments, posts=current_user.Posts, accountType=current_user.AccountType)

@main.route("/images/")
def images():
    return render_template("images.html")

@main.route("/editworldinfo/")
def editworld():
    return render_template("editworldinfo.html")

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

app = create_app()


if __name__ == '__203.main__':
    app.run(debug=True)