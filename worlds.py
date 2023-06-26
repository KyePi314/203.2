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

create = Blueprint('create', __name__)

#Create new world function.
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
        #If else statement for in case the user has already created 2 worlds.
        if (counter >= 2 and current_user.AccountType == "Basic"):
            flash('You cannot have more than two worlds. Please susbcribe for access to more worlds!')
            return redirect(url_for('main.createworld'))
        elif(worldName == "" or worldInfo == ""):
            flash('You cannot leave any of the fields blank!')
            return redirect(url_for('main.createworld'))
        else:
            #Creates a new world and puts it into the database.
            new_world = World(id=worldID, UserName=current_user.UserName, WorldName=worldName, WorldDescription=worldInfo)
            flash('Your world has now been added!')
            session.add(new_world)
            session.commit()
            return redirect(url_for('main.createworld'))

        
@create.route('/deleteworld', methods=['POST', 'GET'])
def deleteworld():

    worlds = session.query(World.WorldName).filter_by(UserName = current_user.UserName).all()
    world_names = [world[0] for world in worlds]  # Extract only the string values

    if request.method == 'POST':
        print("WORKING: ", world_names)
        # Gets the world choice dropdown from the html form
        select = request.form.get('option')
        print("Selected value: ", select)
        if select == "choose":
            print("CHOOSE")
            flash('please choose a world from the dropdown')
            return redirect(url_for('create.deleteworld'))
        else:
            print("WORLD", select)
            #Not working. - HTML page isn't loading list.
            worldname = session.query(World).filter(World.WorldName == select).first()
            session.delete(worldname)
            session.commit()
            flash("This world has been deleted successfully!")
            return redirect(url_for('update.worlds', worlds_list=world_names))
    
    return render_template("deleteworld.html", worlds_list=world_names)



# #Create the Database
# engine = create_engine("sqlite:///database.db", echo=True)
# # #Creates a session.
# Session = sessionmaker(bind=engine)
# session = Session()