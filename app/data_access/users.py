from app.models.user import User

class UserDAO:

    def __init__(self):
        self.valid_users = ['shrayas','gugu']

    def get(self, user_id):
        if user_id in self.valid_users:
            user = User(user_id)
            return user
        else:
            return None

    def validate(self, user_id):
        return user_id in self.valid_users
