from flask_login import UserMixin

class User(UserMixin):
    def create(self, user):
        self.email = user['email']
        self.password = user['password']
        return self

    def get_id(self):
        return self.email

