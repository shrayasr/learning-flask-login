import json

from flask import Flask, render_template, jsonify, request, redirect, \
        url_for, flash
from flask.ext.login import (LoginManager, login_required, logout_user, \
        login_user, current_user)

from users import UserDAO

app = Flask(__name__)
app.secret_key = "SECRET_SHHH"
login_manager = LoginManager()
login_manager.init_app(app)


list_of_customers = [
        {
            "id":1,
            "name":"a"
        },
        {
            "id":2,
            "name":"aa"
        },
        {
            "id":3,
            "name":"aaa"
        },
        {
            "id":4,
            "name":"aaaa"
        }]

customer_details = {
        "1": {
            "age": 1,
            "sex": "m"
            },
        "2": {
            "age": 2,
            "sex": "m"
            },
        "3": {
            "age": 3,
            "sex": "f"
            },
        "4": {
            "age": 4,
            "sex": "f"
            }
        }

@login_manager.user_loader
def load_user(user_name):
    userDAO = UserDAO()
    return userDAO.get(user_name)

@app.route("/")
def index():
    return render_template("index.html", customers=list_of_customers)

@app.route("/whoami")
def whoami():
    user_name = current_user.get_id()
    if user_id is None:
        return "Who are you?"
    else:
        return user_name

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        try:
            user_name = request.form["username"].strip()
            if len(user_name) == 0:
                flash("Enter a username")
                return redirect(url_for("login"))
            else:
                userDAO = UserDAO()
                if userDAO.validate(user_name):
                    print user_name
                    login_user(userDAO.get(user_name))
                    return redirect(url_for("customers"))
                else:
                    flash("Invalid user")
                    return redirect(url_for("login"))
        except Exception as e:
            print e
            return "Fields empty dai"

@app.route("/customers/")
@login_required
def customers():
    return render_template("customers.html", customers=list_of_customers)
    
@app.route("/customers/<id>")
@login_required
def customer(id):
    customer = customer_details.get(str(id))
    return jsonify(customer)

@app.route("/logout/", methods=["POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
