from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
import config


app = Flask(__name__)
CORS(app)

client = MongoClient(config.MONGO_URI)
db = client[config.MONGO_NAME]