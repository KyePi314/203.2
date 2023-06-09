### IMPORTING PACKAGES ###
from flask import Flask, render_template, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_required, current_user, LoginManager
from flask_login import UserMixin
from authentication import auth
from flask_migrate import Migrate, migrate
import os
SECRET_KEY = os.urandom(32)

login_manager = LoginManager()
migrate = Migrate()
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


from models import db, User


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    db.init_app(app)
    migrate.init_app(app, db)
    
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    # Registering the blueprint for the auth routes in the site
    from authentication import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    #Registering the main routes used in the site
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app




app = create_app()



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

if __name__ == '__203.main__':
    app.run(debug=True)