## For log in/sign up actions ##

## Importing important packages ###
from flask import (render_template, request, Blueprint, redirect, session, url_for)
from flask_login import login_user, logout_user, login_required, current_user
import functools
import re
from werkzeug.security import check_password_hash, generate_password_hash

# temp database until proper one hooked up
database = {'User' : {
    1 : {'username' : 'Dean', 'Password' : 666, 'Email' : 'impala@gmail.com'},
}}

currentKey = 1

auth = Blueprint('auth', __name__)
# Temp database info to get login stuff tpio run and load the home page

@auth.route('/login', methods=['GET', 'POST']) # Defining the login page path
def login(): # Log in page function
    msg = ''
    user = request.form.get('username')
    pwd = request.form.get('password')
    if user not in database:
        msg = 'Incorrect Username, please check your details and try again. Or sign up with the button below'
        return render_template('auth/landingpage.html', info='Invalid User!')
    else:
        if database[user] != pwd:
            msg = 'Incorrect Password, please try again or sign up'
            return render_template('auth/landingpage.html')
        else:
            login_user(user)
            return render_template('home.html', name=user)

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    msg = ''
    d = 0
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        user = request.form.get('username')
        pwd = request.form.get('password')
        email = request.form.get('email')
        if user in database and pwd in database:
            msg = 'Account already exists!'
        elif user in database:
            msg = 'Username already taken!'
        elif not user or not pwd or not email:
            msg = 'Please enter details into form'
        else:
            msg = 'Account Successfully Created! You can now log in'
            for x in database.keys():
                if x == currentKey:
                    currentKey += 1
                    database['user'] = {'Username' : user, 'password' : pwd, 'Email' : email}
            currentKey += 1
            print(database)
    elif request.method == 'POST':
        msg = 'Please fill out the form'
    return render_template('auth/signup.html', msg = msg)
