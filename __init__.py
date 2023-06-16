## The init file ##
from flask import Flask, render_template, request, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate, migrate
import os
SECRET_KEY = os.urandom(32)


login_manager = LoginManager()
migrate = Migrate()


# The function that initializes the application and its authentication system/databse 
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
    from models import engine
    migrate.init_app(app, engine)
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # Registering the blueprint for the auth routes in the site
    from UpdateDetails import update as update_blueprint
    app.register_blueprint(update_blueprint)
    from authentication import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    #Registering the main routes used in the site
    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app