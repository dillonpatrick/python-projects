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


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User.query.filter_by(username=username).first()
        login_user(user)

        if user and password == user.password:
            return jsonify({"message": "User authenticated with success."})

    return jsonify({"message": "Invalid credentials."}), 401


@app.route("/meal", methods=["POST"])
@login_required
def meal():
    data = request.json

    meal_name = data.get("name")
    is_diet = data.get("is_diet", False)
    mael_description = data.get("description", "")
    date = data.get("date", datetime.now())

    if meal_name:
        meal = Meal(
            user_id=current_user.id,
            name=meal_name,
            is_diet=is_diet,
            description=mael_description,
            date=date,
        )
        db.session.add(meal)
        db.session.commit()
        return jsonify(
            {"message": "Meal successfully created.", "meal": meal.to_dict()}
        )

    return jsonify({"message": "Invalid request"}), 400


@app.route("/meal/<int:meal_id>", methods=["PUT"])
@login_required
def update_meal(meal_id):
    meal = Meal.query.get(meal_id)

    data = request.json

    if meal and current_user.id == meal.user_id:
        meal.name = data.get("name", meal.name)
        meal.is_diet = data.get("is_diet", meal.is_diet)
        meal.description = data.get("description", meal.description)
        meal.date = data.get("date", meal.date)

        db.session.commit()
        return jsonify({"message": "Meal changed successfully."})

    return jsonify({"message": "Meal not found"}), 404


@app.route("/meal/<int:meal_id>", methods=["DELETE"])
@login_required
def delete_meal(meal_id):
    meal = Meal.query.get(meal_id)

    if meal and current_user.id == meal.user_id:
        db.session.delete(meal)
        db.session.commit()
        return jsonify({"message": "Meal deleted successfully"})

    return jsonify({"message": "Meal not found"}), 404


@app.route("/meal", methods=["GET"])
@login_required
def list_meals():
    meals_list = []
    meals = Meal.query.filter_by(user_id=current_user.id).all()
    for m in meals:
        meals_list.append(
            {
                "id": m.id,
                "user_id": m.user_id,
                "name": m.name,
                "description": m.description,
                "date": str(m.date),
                "is_diet": m.is_diet,
            }
        )

    return jsonify(meals=meals_list)  # retorna o json tratado/formatado certinhos


@app.route("/meal/<int:meal_id>", methods=["GET"])
@login_required
def get_meal(meal_id):
    meal = Meal.query.get(meal_id)

    if meal and current_user.id == meal.user_id:
        meal_user = {
            "id": meal.id,
            "user_id": meal.user_id,
            "name": meal.name,
            "description": meal.description,
            "date": str(meal.date),
            "is_diet": meal.is_diet,
        }
        return jsonify(meal=meal_user)

    return jsonify({"message": "Meal not found."}), 404


if __name__ == "__main__":
    app.run(debug=True)
