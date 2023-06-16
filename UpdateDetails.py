from datetime import datetime
from base64 import b64encode
import base64
from io import BytesIO #Converts data from Database into bytes
from flask import render_template, request, Blueprint, redirect, session, url_for
from models import (engine, User, session, Image)

update = Blueprint('update', __name__)

#### Code for uploading pictures to Image database ####
def render_picture(data):
    render_pic = base64.b64encode(data).decode('ascii')
    return render_pic

@update.route('/Upload', methods=['POST'])
def upload():
    file = request.files['imageFile']
    data = file.read()
    render_file = render_picture(data)
    

