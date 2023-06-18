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
    world = session.query(World).filter_by(UserName = current_user.UserName).all()
    i = []
    for x in world:
        i.append(x.id)  
        print(current_user.id, "  + ", x)
    if request.method == 'POST':
        
        if request.form.get('c1', None) == "world1":
            w1 = min(i)
            world1 = session.query(World).filter_by(w1).first()
            return redirect(url_for('main.worldinfo'))
        elif request.form.get('c2', None) == 'world2':
            pass
        else:
            pass
    elif request.method == 'GET':
        return render_template("worldsPage.html")
    return render_template("worldsPage.html")



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


