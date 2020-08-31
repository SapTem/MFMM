from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import logging
import config
from flask_login import LoginManager, login_user, login_required
from pymongo import MongoClient
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token

app = Flask(__name__)
CORS(app)

client = MongoClient('mongodb://localhost:27017/')
app.config['SECRET_KEY']='secret'
db = client.todoApp
jwt = JWTManager(app)

def isLoginValid(login, msg):
    status = config.ok
    for simbol in config.logValid: 
        if not simbol in login or ' ' in login:
            status = config.err
            msg.append(config.invalidLoginFormat)
            break
    if config.minLoginLen > len(login) or len(login) > config.maxLoginLen:
        status = config.err
        msg.append(config.invalidLoginLen)
    return status, msg

def isPassValid(password, msg):
    status = config.ok
    if config.minPassLen > len(password) or len(password) > config.maxPassLen:
        status = config.err
        msg.append(config.invalidPassLen)
    if ' ' in password:
        status = config.err
        msg.append(config.invalidPassSpace)
    return status, msg
    
def isNameValid(name, msg):
    status = config.ok
    if config.minNameLen > len(name) or len(name) > config.maxNameLen:
        status = config.err
        msg.append(config.invalidNameLen)
    return status, msg


def isFormValid(whatForm, email, password, name=''):
    msg=[]
    statuslog, msg= isLoginValid(email, msg)
    statusPass, msg = isPassValid(password, msg)
    if whatForm == config.reg:
        statusName, msg = isNameValid(name, msg)
        status = (config.ok if statuslog == statusPass == statusName == config.ok else  config.err)
    else:
        status = (config.ok if statuslog == statusPass == config.ok else  config.err)
    return status, msg


@app.route("/registr", methods=["POST"])
def registr():
    data = request.get_json()
    status, msg = isFormValid(config.reg, data.get("email"), data.get("pass"), data.get("name"))
    if status == config.ok:
        db.login.insert_one({
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

    status, msg = isFormValid(config.log, _email, _pass)
    if status == config.err:
        return responseMapper(status,msg)
        
    try:
        res = db.login.find_one({"email" : _email})
        if res:
            if check_password_hash(res["password"] , _pass):
                access_tocken = create_access_token(identity={
                    "name":_email,
                    "pass": _pass
                }) 
                db.tocken.insert_one({
                    "email": _email,
                    "tocken": access_tocken
                })
                return responseMapper(config.ok, config.successAuth, access_tocken)
            else:
                return responseMapper(config.err,config.invalidPass)
        else:
            return responseMapper(config.err,config.undefinedUser)       
    except:
        return responseMapper(config.err,config.serverErr),400


@app.route("/isAuth", methods=["POST"])
def isAuth():
    print(request.get_json().get("access_tocken"))
    if db.tocken.find_one({"tocken": request.get_json().get("access_tocken")}):
        return responseMapper(config.auth)
    else:
        return responseMapper(config.err,"noAuth")


@app.route("/logOut", methods=["POST"])
def logOut():
    access_tocken = request.get_json().get("access_tocken")
    db.tocken.delete_many({"tocken": access_tocken})
    

def responseMapper(status, errMessage="ok", access_tocken=''):
    return jsonify({
        "status" : status,
        "errorMsg": errMessage,
        "access_tocken": access_tocken
    })




