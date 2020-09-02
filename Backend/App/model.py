from App import db

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     password_hash = db.Column(db.String(128))

#     def __repr__(self):
#         return '<User {}>'.format(self.username) 

def addUser(name, email, hpass):
    db.login.insert_one({
            "name": name,
            "email": email,
            "password": hpass
        })

def addTocken(_email, access_tocken):
    db.tocken.insert_one({
        "email": _email,
        "tocken": access_tocken
    })

def deleteTocken(access_tocken):
    db.tocken.delete_many({"tocken": access_tocken})

def isTocken(access_tocken):
    return True if db.tocken.find_one({"tocken": access_tocken}) else False