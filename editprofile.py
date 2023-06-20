
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

#Must fix tomorrow.
#Not currently working:
@profile.route('/changeemail', methods=['GET', 'POST'])
def changeemail():
    if request.method == 'GET':
        return render_template('userprofile.html')
    else:
        newemail = request.form.get('email')
        sameemail = session.query(User).filter_by(Email=newemail).first()
        user = session.query(User).filter(User.UserName == current_user.UserName).first()
        if(newemail == current_user.Email):
            flash("Email cannot be the same!")
            return redirect(url_for('main.userprofile'))
        elif sameemail:
            flash("Email currently in use already!")
            return redirect(url_for('main.userprofile'))
        else:
            user.Email = newemail
            session.commit()
            flash("Email changed successfully!")
            return redirect(url_for('main.userprofile'))



@profile.route('/changepass', methods=['POST'])
def changepass():
        #Placeholder for now.
    newpass = request.form.get('password')
    confirmpass = request.form.get('confirmpassword')
    if(newpass != confirmpass):
        flash("The passwords must be matching!")
        return redirect(url_for('main.userprofile'))
    else:
        user = session.query(User).filter(User.UserName == current_user.UserName).first()
        password = generate_password_hash(newpass, method='sha1')
        user.Password = password
        session.commit()
        flash("Password changed successfully!")
        return redirect(url_for('main.userprofile')) 