from App import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, name, email, password_hash):
        self.name = name
        self.email = email
        self.password_hash = password_hash

    def __repr__(self):
        return self.email 

class Tocken(db.Model):
    email = db.Column(db.String(120), index=True ,unique=True)
    access_tocken = db.Column(db.String(450), index=True, primary_key=True)

    def __init__(self, email, access_tocken):
        self.email = email
        self.access_tocken = access_tocken

    def __repr__(self):
        return self.email 


