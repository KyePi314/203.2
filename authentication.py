## For log in/sign up actions ##
## Importing important packages ###
from hashlib import pbkdf2_hmac
from flask import (render_template, request, Blueprint, redirect, session, url_for, flash)
from flask_login import login_user, logout_user, login_required, current_user
from models import engine, User, session
from __init__ import login_manager
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import delete


auth = Blueprint('auth', __name__)




@auth.route('/login', methods=['GET', 'POST']) # Defining the login page path
def login(): # Log in page function
    if request.method == 'GET':
        return render_template('auth/login.html')
    else:
        name = request.form.get('username')
        pwd = request.form.get('password')
        remember = True if request.form.get('remember') else False
        user = session.query(User).filter_by(UserName=name).first()
        if not user:
            flash('Account does not exist! Please sign up to continue')
            return redirect(url_for('auth.signup'))
        elif not check_password_hash(user.Password, pwd):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login')) 
        if name == "" or pwd == "":
            flash('Please fill out form!')
        login_user(user, remember=remember)
        return redirect(url_for('main.home', username=user.UserName))

@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method ==  'GET':
        return render_template('auth/signup.html')
    else:
        name = request.form.get('username')
        pwd = request.form.get('password')
        email = request.form.get('email')
        pwd_check = request.form.get('pwd-check')
        user = session.query(User).filter_by(Email=email).first()
        rows = session.query(User).count()
        userId = rows + 1
        if name == "" or pwd == "" or email == "":
            flash('Please fill out form!')
            return redirect(url_for('auth.signup'))
        elif pwd != pwd_check:
            flash('please make sure the passwords match')
            return redirect(url_for('auth.signup'))
        elif user:
            flash('Email is already in use with an existing account!')
            return redirect(url_for('auth.signup'))
        password = generate_password_hash(pwd, method='sha1')
        new_user = User(id=userId, Email=email, UserName=name, Password=password,  Mana=0, Awards=0, Posts=0, AccountType="Basic", Comments=0)
        session.add(new_user)
        session.commit()
        return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

from models import User

@login_manager.user_loader
def load_user(user_id):
    user = session.query(User).filter_by(UserName=user_id).first()
    if user is not None:
        return user
    else:
        return None
    

