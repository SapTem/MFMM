from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:admin@localhost/toDoApp'
db = SQLAlchemy(app)
app.config['SECRET_KEY']='secret'
jwt = JWTManager(app)


from App import routes