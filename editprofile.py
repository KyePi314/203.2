
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, delete
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from flask import (render_template, request, Blueprint, redirect, session, url_for, flash)
from flask_login import current_user
from models import World, User, session
import sqlalchemy
from sqlalchemy.orm import sessionmaker

#Way of handling routing that connect to the main app.
profile = Blueprint('profile', __name__)

#Change email function.
@profile.route('/changeemail', methods=['GET', 'POST'])
def changeemail():
    if request.method == 'GET':
        return render_template('userprofile.html')
    else:
        newemail = request.form.get('email')
        sameemail = session.query(User).filter_by(Email=newemail).first()
        user = session.query(User).filter(User.UserName == current_user.UserName).first()
        #If else statements in case the user accidentally has the same email as someone else or the same as their current one.
        if(newemail == current_user.Email):
            flash("Email cannot be the same!")
            return redirect(url_for('main.userprofile'))
        elif sameemail:
            flash("Email currently in use already!")
            return redirect(url_for('main.userprofile'))
        else:
            #Updates the email in the database for the user and sends a message of the success.
            user.Email = newemail
            session.commit()
            flash("Email changed successfully!")
            return redirect(url_for('main.userprofile'))

#Change password function.
@profile.route('/changepass', methods=['POST'])
def changepass():

    newpass = request.form.get('password')
    confirmpass = request.form.get('confirmpassword')
    #If else statement in case the passwords aren't matching.
    if(newpass != confirmpass):
        flash("The passwords must be matching!")
        return redirect(url_for('main.userprofile'))
    else:
        #Updates the database.
        user = session.query(User).filter(User.UserName == current_user.UserName).first()
        password = generate_password_hash(newpass, method='sha1')
        user.Password = password
        session.commit()
        flash("Password changed successfully!")
        return redirect(url_for('main.userprofile')) 