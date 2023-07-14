from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://user:userpass@mycluster.xntmcj2.mongodb.net/responsi?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route("/")
def index():
    users = mongo.db.users.find({})
    return render_template('index.html', users = users)
