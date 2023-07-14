from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["SECRET_KEY"] = "286c57c114d31b2c3acf75599aef1e2af751a817"
app.config["MONGO_URI"] = "mongodb+srv://user:userpass@mycluster.xntmcj2.mongodb.net/"

mongodb_client = PyMongo(app)
db = mongodb_client.db

from responsi import routes