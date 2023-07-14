from responsi import app
from flask import render_template

from responsi import db

@app.route("/")
def index():
    users= []
    for user in db.responsi.find():
        user["name"] = str(user["name"])

    return render_template('index.html')