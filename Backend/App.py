from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import logging
import config

from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://localhost:27017/')
db = client.todoApp
login = db.login


def isLoginValid(login, msg):
    status = "success"
    for simbol in config.logValid: 
        if not simbol in login or ' ' in login:
            status = "error"
            msg.append(config.invalidLoginFormat)
            break
    if config.minLoginLen > len(login) or len(login) > config.maxLoginLen:
        status = "error"
        msg.append(config.invalidLoginLen)
    return status, msg

def isPassValid(password, msg):
    status = "success"
    if config.minPassLen > len(password) or len(password) > config.maxPassLen:
        status = "error"
        msg.append(config.invalidPassLen)
    if " " in password:
        status = "error"
        msg.append(config.invalidPassSpace)
    return status, msg
    
def isNameValid(name, msg):
    status = "success"
    if config.minNameLen > len(name) or len(name) > config.maxNameLen:
        status = "error"
        msg.append(config.invalidNameLen)
    return status, msg

@app.route("/registr", methods=["POST"])
def registr():
    data = request.get_json()
    msg=[]
    statuslog, msg= isLoginValid(data.get("email"), msg)
    statusPass, msg = isPassValid(data.get("pass"), msg)
    statusName, msg = isNameValid(data.get("name"), msg)
    status = ("success" if statuslog == statusPass == statusName == "success" else  "error")
    print(status,msg)
    if status == "success":
        login.insert_one({
            "name":data.get("name"),
            "email":data.get("email"),
            "password": generate_password_hash(data.get("pass"))
        })
    return responseMapper(status, msg)


@app.route("/login", methods=["POST"])
def isLogin():
    data = request.get_json()
    _email = data.get("email")
    _pass = data.get("pass")
    try:
        user = login.find_one({"email" : _email})
        print(bool(user))
        if user:
            if (check_password_hash(user["password"] , _pass)):
                return jsonify({"status": "success", "authorizated":True, "pass": True})
            else:
                return jsonify({"status" : "success", "authorizated": True, "pass": False})
        else:
            return jsonify({"status" : "success", "authorizated": False, "pass": False})        
    except:
        return jsonify({"status" : "error", "authorizated": False, "pass": False}),400

    
def responseMapper(status, errMessage="ok"):
    return jsonify({
        "status" : status,
        "errorMsg": errMessage
    })




app.run()