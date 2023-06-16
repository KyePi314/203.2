
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR, delete
from sqlalchemy.ext.declarative import declarative_base
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import check_password_hash, generate_password_hash
from flask import (render_template, request, Blueprint, redirect, session, url_for, flash)
from flask_login import current_user
from models import World, User
import sqlalchemy
from sqlalchemy.orm import sessionmaker

createworld = Blueprint('createworld', __name__)

@createworld.route('/createworld', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('/createworld.html')
    else:
        counter = 0

        worldName = request.form.get('worldName')
        worldInfo = request.form.get('worldInfo')
        world = session.query(World).filter(World.UserName == current_user)
        for item in world:
            counter += 1
        if (counter <= 2):
            flash('You cannot have more than two worlds. Please susbcribe for access to more worlds!')
            return redirect(url_for('createworld'))
        elif(worldName == "" or worldInfo == ""):
            flash('You cannot leave any of the fields blank!')
            return redirect(url_for('createworld'))
        else:
            new_world = World(UserName=current_user, WorldName=worldName, WorldDescription=worldInfo)
            flash('Your world has now been added!')
            session.add(new_world)
            session.commit()
            return redirect(url_for('createworld'))



# #Create the Database
# engine = create_engine("sqlite:///database.db", echo=True)
# # #Creates a session.
# Session = sessionmaker(bind=engine)
# session = Session()