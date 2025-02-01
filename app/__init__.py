# Initializes the Flask app 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
api = Api(app)

from app import routes

db.create_all()
