from datetime import datetime

from database import db
from flask import Flask, jsonify, request
from flask_login import LoginManager, current_user, login_required, login_user
from models.meal import Meal
from models.user import User

login_manager = LoginManager()
app = Flask(__name__)

app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:admin123@127.0.0.1:3306/daily-diet"
)


db.init_app(app)
login_manager.init_app(app)


login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == "__main__":
    app.run(debug=True)
