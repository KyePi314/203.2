from datetime import datetime
from base64 import b64encode
import base64
from io import BytesIO #Converts data from Database into bytes
from flask import render_template, request, Blueprint, redirect, session, url_for, flash
from models import (engine, User, session, Img, World)
from flask_login import current_user, login_required


update = Blueprint('update', __name__)
### Code that handles getting the correct world ###
@update.route("/worldspage", methods=['POST', 'GET'])
def worlds():
    return render_template("worldsPage.html")

@update.route("/worldinfo/", methods=['POST', 'GET'])
def worldinfo():
    # Finds the worlds saved to the user currently logged in
    world = session.query(World.id).filter_by(UserName = current_user.UserName).all()
    i = []
    # saves the id's of the found worlds in the list
    for x in world:
        i.append(x.id)  
    # Gets the world choice dropdown from the html form
    select = request.form.get('options')
    if request.method == 'POST':
         # Worlds are identified by their id's, lowest number to largest
        if select == "one":
            w1 = min(i)
            world1 = session.query(World).filter_by(id = w1).first()
            return render_template("worldinfo.html", WorldName=world1.WorldName, description=world1.WorldDescription)
        if select == 'two':
            w2 = max(i)
            world2 = session.query(World).filter_by(id = w2).first()
            return render_template("worldinfo.html", WorldName=world2.WorldName, description=world2.WorldDescription)
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
    return redirect(url_for('main.worlds'))


