from flask import Flask, request

from flask.ext.login import (LoginManager, login_required, logout_user, 
        login_user, current_user)

from app.data_access.users import UserDAO

app = Flask(__name__)
app.secret_key="WHATTE_SECRET_KEY_PA"
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
    userDAO = UserDAO()
    return userDAO.get(userid)

@app.route("/")
def hello():
    return "Hello"

@app.route("/whoami")
def whoami():
    user_id = current_user.get_id()
    if user_id == None:
        return "No one logged in"
    else:
        return user_id

@app.route("/login")
def login():

    user_name = request.args.get("user_name", None)

    if user_name == None:
        return "Need user_name"
    else:
        userDAO = UserDAO()
        
        if userDAO.validate(user_name) == True:
            login_user(userDAO.get(user_name))
            return "user logged in!"
        else:
            return "Invalid user_name"

@app.route("/settings")
@login_required
def settings():
    return "Settings screen"

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return "Logged out!"

if __name__ == "__main__":
    app.run(debug=True)
