## For log in/sign up actions ##

## Importing important packages ###
from flask import (render_template, request, Blueprint, redirect, session, url_for, flash)
from flask_login import login_user, logout_user, login_required, current_user
import functools
from werkzeug.security import check_password_hash, generate_password_hash
from __init__ import database

auth = Blueprint('auth', __name__)
# Temp database info to get login stuff to run and load the home page

@auth.route('/login', methods=['GET', 'POST']) # Defining the login page path
def login(): # Log in page function
    user = request.form['username']
    pwd = request.form['password']
    if user not in database:
        return render_template('auth/landingpage.html', info='Invalid User!')
    else:
        if database[user] != pwd:
            return render_template('auth/landingpage.html', info='Invalid Password!')
        else:
            return render_template('home.html', name=user)