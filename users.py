from models import User

class UserDAO:

    def __init__(self):
        self.valid_users = ['foo','bar']

    def get(self, user_name):
        if user_name in self.valid_users:
            user = User(user_name)
            return user
        else:
            return None

    def validate(self, user_name):
        return user_name in self.valid_users
