## For log in/sign up actions ##

## Importing important packages ###
from flask import (render_template, request, Blueprint, redirect, session, url_for, flash)
from flask_login import login_user, logout_user, login_required, current_user
import functools
from werkzeug.security import check_password_hash, generate_password_hash

auth = Blueprint('auth', __name__)
# Temp database info to get login stuff to run and load the home page

       