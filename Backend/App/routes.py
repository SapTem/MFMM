from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

from App import app, jwt, config
from App.isValidMethod import isFormValid, isLoginValid, isNameValid, isPassValid
from App.mapper import responseMapper
from App.model import *

@app.route("/registr", methods=["POST"])
def registr():
    data = request.get_json()
    status, msg = isFormValid(config.reg, data.get("email"), data.get("pass"), data.get("name"))
    if status == config.ok:
        user = User(data.get("name"), data.get("email"), generate_password_hash(data.get("pass")))
        db.session.add(User(data.get("name"), data.get("email"), generate_password_hash(data.get("pass"))))
        db.session.commit()
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
        user = User.query.filter_by(email=_email).first()
        if user :
            if check_password_hash(user.password_hash , _pass):
                access_tocken = create_access_token(identity={
                    "name":_email,
                    "pass": _pass
                }) 
                tocken = Tocken(_email, access_tocken)
                db.session.add(tocken)
                db.session.commit()
                return responseMapper(config.ok, config.successAuth, access_tocken)
            else:
                return responseMapper(config.err,config.invalidPass)
        else:
            return responseMapper(config.err,config.undefinedUser)       
    except:
        return responseMapper(config.err,config.serverErr),400


@app.route("/isAuth", methods=["POST"])
def isAuth():
    user = Tocken.query.filter_by(access_tocken=request.get_json().get("access_tocken")).first()
    if user:
        return responseMapper(config.auth)
    else:
        return responseMapper(config.err,"noAuth")


@app.route("/logOut", methods=["POST"])
def logOut():
    access_tocken = request.get_json().get("access_tocken")
    tocken = Tocken.query.filter_by(access_tocken = access_tocken).one()
    db.session.delete(tocken)
    db.session.commit()
    return responseMapper(config.successDeleted)
    
    






