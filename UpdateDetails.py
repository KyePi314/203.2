from datetime import datetime
from base64 import b64encode
import base64
from io import BytesIO #Converts data from Database into bytes
from flask import render_template, request, Blueprint, redirect, session, url_for, flash
from models import (engine, User, session, Img, World, Culture, History, Timeline, Religion, Species)
from flask_login import current_user, login_required


update = Blueprint('update', __name__)
### Code that handles getting the correct world ###
@update.route("/worldspage", methods=['POST', 'GET'])
def worlds():
    worlds = session.query(World.WorldName).filter_by(UserName = current_user.UserName).all()
    world_names = [world[0] for world in worlds]  # Extract only the string values
    
    return render_template("worldsPage.html", worlds_list=world_names)

@update.route("/worldinfo/", methods=['POST'])
def worldinfo():
    # Finds the worlds saved to the user currently logged in
    worlds = session.query(World).filter_by(UserName = current_user.UserName).all()
    i = []
    # saves the id's of the found worlds in the list
    for x in worlds:
        i.append(x.id)  
    
    if request.method == 'POST':
        # Gets the world choice dropdown from the html form
        select = request.form.get('option')
        print("Selected value: ", select)
        if select == "choose":
            flash('please choose a world from the dropdown')
            return redirect(url_for('update.worlds'))
        else:
            ## Getting all the details to fill out the HTML page
            world = session.query(World).filter_by(WorldName=select).first()
            culture = session.query(Culture).filter_by(WorldName=select).first()
            history = session.query(History).filter_by(WorldName=select).first()
            timelines = session.query(Timeline).filter_by(WorldName=select).first()
            religion = session.query(Religion).filter_by(WorldName=select).first()
            species = session.query(Species).filter_by(WorldName=select).first()

            return render_template("worldinfo.html", WorldName=world.WorldName, description=world.WorldDescription, Culture_details=culture.CultureTitle if culture else None, History_details=history.HistoryTitle if history else None, Timeline_details=timelines.TimelineTitle if timelines else None, Species_details=species.SpeciesTitle if species else None, Religions_details=religion.ReligionTitle if religion else None)
    return render_template("worldinfo.html")


#### Code for uploading pictures to Image database ####
def render_picture(data):
    render_pic = base64.b64encode(data).decode('ascii')
    return render_pic

@update.route('/Update', methods=['POST'])
def Update():
    img = request.files['imageFile']
    data = img.read()
    render_file = render_picture(data)
    rows = session.query(Img).count()
    imgId = rows + 1
    imgFile = Img(id=imgId, UserName=current_user.UserName, data=data, rendered_data=render_file)
   
    session.add(imgFile)
    session.commit()
    return redirect(url_for('update.worlds'))


