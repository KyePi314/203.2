### IMPORTING PACKAGES ###
from flask import Flask, render_template, request
from flask_login import login_required, current_user

import os

app = Flask(__name__)



@app.route("/")
def index():
    return render_template("auth/landingpage.html")

@app.route("/landingpage/")
def logout():
    return render_template("auth/landingpage.html")

@app.route("/home/")
def home():
    return render_template('home.html')

@app.route("/contact/")
def contact():
    return render_template("Contact.html")

@app.route("/Issues/")
def issues():
    return render_template("Issues.html")

@app.route("/Maps/")
def maps():
    return render_template("Maps.html")

@app.route("/subscription/")
def subscription():
    return render_template("SubscriptionPage.html")

@app.route("/Timeline/")
def timeline():
    return render_template("Timeline.html")
   
@app.route("/worldsPage/")
def worlds():
    return render_template("worldsPage.html")

@app.route("/worldinfo/")
def worldInfo():
    return render_template("worldinfo.html")

@app.route("/userprofile/")
def userprofile():
    return render_template("userProfile.html")

####### Login code - WILL BE MOVED WHEN WORKING ON PROPER PYTHON FUNCTIONALITY - (-kye) ########

database = {'Jane':'123',
            'Dean':'666', 'Ollie':'999'}

@app.route('/login', methods=['GET', 'POST']) # Defining the login page path
def login(): # Log in page function
    user = request.form['username']
    pwd = request.form['password']
    if user not in database:
        return render_template('auth/landingpage.html', info='Invalid User!')
    else:
        if database[user] != pwd:
            return render_template('auth/landingpage.html', info='Invalid Password!')
        else:
            return render_template('home.html', name=user)

if __name__ == '__203.main__':
    app.run(debug=True)
