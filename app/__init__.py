import os
from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy

UPLOAD_FOLDER = "app/static/filefolder"
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
from flask.ext.marshmallow import Marshmallow
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://avogzdlajafwwd:pzWChTjmvTtZJ6W2PCQg8tSXsE@ec2-107-20-234-127.compute-1.amazonaws.com:5432/d267het21etqvv'
db = SQLAlchemy(app)


from app import views, models
