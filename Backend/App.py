from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import logging
import config
from flask_login import LoginManager, login_user, login_required

from pymongo import MongoClient
from moduls import User
app = Flask(__name__)
CORS(app)

Login_manager = LoginManager()
Login_manager.init_app(app)

client = MongoClient('mongodb://localhost:27017/')
db = client.todoApp
login = db.login

app.config['SECRET_KEY']='secret'

@LoginManager.user_loader
def load_user(user_id):
    return User.get(user_id)

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
        res = login.find_one({"email" : _email})
        if res:
            if (check_password_hash(res["password"] , _pass)):
                user = User().create(res)
                login_user(user)
                return responseMapper("success","Успешно авторизован!")
            else:
                return responseMapper("error","Пароль не верный!")
        else:
            return responseMapper("error","Пользователь не найден!")       
    except:
        return responseMapper("error","Соединение с сервером не установлено!"),400


@app.route("/isAuth")
@login_required
def isAuth():
    print("dsssssssssssssssdfsdfsf")
    return jsonify({
        "isAuth":True
    })
    
def responseMapper(status, errMessage="ok"):
    return jsonify({
        "status" : status,
        "errorMsg": errMessage
    })




app.run()