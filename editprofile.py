
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, delete
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from flask import (render_template, request, Blueprint, redirect, session, url_for, flash)
from flask_login import current_user
from models import User, session
import sqlalchemy
from sqlalchemy.orm import sessionmaker

profile = Blueprint('profile', __name__)


#Not currently working:
@profile.route('/changeemail', methods=['GET', 'POST'])
def editEmail():
    if request.method == 'GET':
        print("Error GET")
        return render_template('userProfile.html')
    else:
        print("Error POST")
        newemail = request.form.get('email')

        user = session.query(User).filter(User.UserName == current_user.name)
        user.Email = newemail
        session.commit()
        flash("Email changed successfully!")
        return redirect(url_for('main.userprofile'))

@profile.route('/changepass', methods=['GET', 'POST'])
def editPass():
    if request.method == 'GET':
        return render_template('userProfile.html')
    else:
        #Placeholder for now.
        newpass = request.form.get('password')
        confirmpass = request.form.get('confirmpassword')
        if(newpass != confirmpass):
            flash("The passwords must be matching!")
            return redirect(url_for('main.userprofile'))
        else:
            user = session.query(User).filter(User.UserName == current_user.name)
            user.Password = newpass
            session.commit()
            flash("Password changed successfully!")
            return redirect(url_for('main.userprofile'))