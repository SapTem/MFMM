from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app)


client = MongoClient('mongodb://localhost:27017/')
app.config['SECRET_KEY']='secret'
db = client.todoApp
jwt = JWTManager(app)


from App import routes