
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
from UpdateDetails import exportworldname

create = Blueprint('create', __name__)

@create.route('/createworld', methods=['GET', 'POST'])
def createworld():
    if request.method == 'GET':
        return render_template('createworld.html')
    else:
        counter= 0
        rows = session.query(World).count() # Gets the number of rows
        worldID = rows + 1 # Will be used to increment the number of rows by one via the ID column, allowing users to have multiple saved rows of data
        worldName = request.form.get('worldName')
        worldInfo = request.form.get('worldInfo')
        world = session.query(World).filter(World.UserName == current_user.UserName)
        for item in world:
            counter += 1
        if (counter >= 2):
            flash('You cannot have more than two worlds. Please susbcribe for access to more worlds!')
            return redirect(url_for('main.createworld'))
        elif(worldName == "" or worldInfo == ""):
            flash('You cannot leave any of the fields blank!')
            return redirect(url_for('main.createworld'))
        else:
            new_world = World(id=worldID, UserName=current_user.UserName, WorldName=worldName, WorldDescription=worldInfo)
            flash('Your world has now been added!')
            session.add(new_world)
            session.commit()
            return redirect(url_for('main.createworld'))

        
@create.route('/deleteworld', methods=['POST'])
def deleteworld():

    #Error: werkzeug.routing.exceptions.BuildError: Could not build url for endpoint 'main.editworldinfo'. Did you mean 'main.createworld' instead?
    worldname = session.query(World).filter(World.WorldName == exportworldname).first()
    session.delete(worldname)
    session.commit()
    flash("This world has been deleted successfully!")
    return redirect(url_for('main.editworldinfo'))
        


# #Create the Database
# engine = create_engine("sqlite:///database.db", echo=True)
# # #Creates a session.
# Session = sessionmaker(bind=engine)
# session = Session()