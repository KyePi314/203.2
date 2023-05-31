### IMPORTING PACKAGES ###
from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("landingpage.html")

@app.route("/home/")
def home():
    return render_template("home.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

@app.route("/Issues/")
def issues():
    return render_template("Issues.html")

@app.route("/Maps/")
def maps():
    return render_template("Maps.html")

@app.route("/SubscriptionPage/")
def subscription():
    return render_template("SubscriptionPage.html")

@app.route("/Timeline/")
def timeline():
    return render_template("Timeline.html")