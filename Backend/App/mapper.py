from flask import jsonify


def responseMapper(status, errMessage="ok", access_tocken=''):
    return jsonify({
        "status" : status,
        "errorMsg": errMessage,
        "access_tocken": access_tocken
    })