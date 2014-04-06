from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, user_name):
        self.user_name = user_name

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return True

    def get_id(self):
        return self.user_name
