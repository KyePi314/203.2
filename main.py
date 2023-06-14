### IMPORTING PACKAGES ###
from flask import Flask, render_template, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, current_user, LoginManager
from flask_login import UserMixin
from __init__ import create_app



main = Blueprint('main', __name__)


@main.route("/")
def index():
    return render_template("landingpage.html")

@main.route("/home/")
def home():
    return render_template('home.html')

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
def worldInfo():
    return render_template("worldinfo.html")

@main.route("/userprofile/")
def userprofile():
    return render_template("userProfile.html")

@main.route("/images/")
def images():
    return render_template("images.html")

app = create_app()




if __name__ == '__203.main__':
    app.run(debug=True)