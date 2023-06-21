from datetime import datetime
from base64 import b64encode
import base64
from io import BytesIO #Converts data from Database into bytes
from flask import render_template, request, Blueprint, redirect, session, url_for, flash
from models import (engine, User, session, Img, World, Culture, History, Timeline, Religion, Species, Post)
from flask_login import current_user, login_required
from sqlalchemy import MetaData

update = Blueprint('update', __name__)

@update.route('/Post', methods=['GET', 'POST'])
@login_required
def post():
    if request.method == 'POST':
        title = request.form.get("title")
        content = request.form.get("content")
        rows = session.query(Post).count()
        postID = rows + 1
        new_post = Post(UserName=current_user.UserName, id=postID, title=title, content=content)
        session.add(new_post)
        session.commit()
        return redirect(url_for("main.home"))
    return render_template("Post.html")


### Code that handles getting the correct world ###
@update.route("/worldspage", methods=['POST', 'GET'])
def worlds():
    worlds = session.query(World.WorldName).filter_by(UserName = current_user.UserName).all()
    world_names = [world[0] for world in worlds]  # Extract only the string values
    
    return render_template("worldsPage.html", worlds_list=world_names)

@update.route("/worldinfo/", methods=['POST'])
def worldinfo():
    if request.method == 'POST':
        # Gets the world choice dropdown from the html form
        select = request.form.get('option')
        print("Selected value: ", select)
        if select == "choose":
            flash('please choose a world from the dropdown')
            return redirect(url_for('update.worlds'))
        else:
            url = url_for('update.culture', WorldName=select)
            ## Getting all the details to fill out the HTML page
            world = session.query(World).filter_by(WorldName=select).first()
            culture = session.query(Culture).filter_by(WorldName=select).first()
            history = session.query(History).filter_by(WorldName=select).first()
            timelines = session.query(Timeline).filter_by(WorldName=select).first()
            religion = session.query(Religion).filter_by(WorldName=select).first()
            species = session.query(Species).filter_by(WorldName=select).first()

            return render_template("worldinfo.html", WorldName=world.WorldName, description=world.WorldDescription, Culture_details=culture.CultureTitle if culture else None, History_details=history.HistoryTitle if history else None, Timeline_details=timelines.TimelineTitle if timelines else None, Species_details=species.SpeciesTitle if species else None, Religions_details=religion.ReligionTitle if religion else None)
    

@update.route("/culture/", methods=['GET', 'POST'])
def culture():
    worldname = request.args.get("WorldName")
    return render_template("culture.html", WorldName=worldname)

@update.route("/specificDetails/", methods=['GET', 'POST'])
def specificDetails():
    worldname = request.args.get("WorldName")
    if request.method == 'POST':
        select = request.form.get('choose_detail')
        title =  request.form.get('title')
        description = request.form.get('detail_description')
        if title != '' and description != '':
            if select == "choose":
                flash('please choose a detail to edit from the dropdown')
                return redirect(url_for('update.worlds'))
            if select == 'Culture':
                rows = session.query(Culture).count()
                rowID = rows + 1
                update_details = session.query(Culture).filter_by(WorldName = worldname).first()
                if update_details:
                    update_details.CultureTitle=title
                    update_details.CultureDescription=description
                else:
                    update_details = Culture(id=rowID, UserName=current_user.UserName, WorldName=worldname, CultureTitle=title, CultureDescription=description)
                    session.add(update_details)
                return redirect(url_for('update.culture', details=update_details, WorldName=worldname))
            elif select == 'History':
                pass
            elif select == 'Religion':
                pass
            elif select == 'Species':
                pass
            elif select == 'Timeline':
                pass    


#### Code for uploading pictures to Image database and updating the world's details ####
def render_picture(data):
    render_pic = base64.b64encode(data).decode('ascii')
    return render_pic

@update.route("/editworldinfo/", methods=['POST', 'GET'])
def editworld():
    world_name = request.args.get('WorldName')
    if request.method == 'POST':
        new_name = request.form.get('name')
        new_description = request.form.get('worldDetails')
        world_name = request.form.get('worldName')
        print("FORM: ", world_name)
        if 'imageFile' in request.files:
            img = request.files['imageFile']
            data = img.read()
            render_file = render_picture(data)
            rows = session.query(Img).count()
            imgId = rows + 1
            imgFile = Img(worldName=new_name if new_name else world_name, id=imgId, UserName=current_user.UserName, data=data, rendered_data=render_file)
            session.add(imgFile)
        updateWorld = session.query(World).filter_by(WorldName = world_name).first()
        if new_name != "":
            updateWorld.WorldName = new_name
        if new_description != "":
            updateWorld.WorldDescription = new_description 
        
        session.commit()
        return redirect(url_for('update.worlds'))
    
    return render_template("editworldinfo.html", worldName=world_name)
    


