## For log in/sign up actions ##

## Importing important packages ###
from flask import (render_template, request, Blueprint, redirect, session, url_for, flash)
import functools
from werkzeug.security import check_password_hash, generate_password_hash

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/login', methods=['GET', 'POST']) # Defining the login page path
def login(): # Log in page function
    return render_template('home.html')
        ### I'll finish this when doing python stuff next meeting - Kye  ###