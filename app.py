from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/Home/")
def home():
    return render_template("Home.html")

@app.route("/Contact/")
def home():
    return render_template("Contact.html")

@app.route("/Issues/")
def home():
    return render_template("Issues.html")

@app.route("/Maps/")
def home():
    return render_template("Maps.html")

@app.route("/SubscriptionPage/")
def home():
    return render_template("SubscriptionPage.html")

@app.route("/Timeline/")
def home():
    return render_template("Timeline.html")