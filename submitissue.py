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
from datetime import datetime
from datetime import date

issue = Blueprint('issue', __name__)

currentdate = date.today()
time = datetime.now()
message = "Thank you for submitting an issue. An admin will get back to you soon. Issue Report sent at {}.".format(time, currentdate)

@issue.route('/submitissue', methods=['POST'])
def submitissue():
        #Temporary
    flash(message)
    return render_template('issues.html')