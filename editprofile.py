
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
@profile.route('/userprofile', methods=['GET', 'POST'])
def userprofile():
    if request.method == 'GET':
        return render_template('userprofile.html')
    else:
        newemail = request.form.get('email')
        sameemail = session.query(User).filter_by(Email=newemail).first()
        user = session.query(User).filter(User.UserName == current_user.UserName).first()
        if(newemail == current_user.Email):
            flash("Email is the same.")
            return redirect(url_for('main.userprofile'))
        elif sameemail:
            flash("Email currently in use already!")
            return redirect(url_for('main.userprofile'))
        else:
            user.Email = newemail
            session.commit()
            flash("Email changed successfully!")
            return redirect(url_for('main.userprofile'))



@profile.route('/changepass', methods=['GET', 'POST'])
def changepass():
    if request.method == 'GET':
        return render_template('userprofile.html')
    else:
        #Placeholder for now.
        newpass = request.form.get('password')
        confirmpass = request.form.get('confirmpassword')
        if(newpass != confirmpass):
            flash("The passwords must be matching!")
            return redirect(url_for('main.userprofile'))
        else:
            user = session.query(User).filter(User.UserName == current_user.UserName).first()
            user.Password = newpass
            session.commit()
            flash("Password changed successfully!")
            return redirect(url_for('main.userprofile')) 