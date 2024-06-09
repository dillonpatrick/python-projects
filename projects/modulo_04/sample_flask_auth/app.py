from flask import Flask, request, jsonify
import bcrypt
from flask import Flask, jsonify, request
from flask_login import (LoginManager, current_user, login_required,
                         login_user, logout_user)

from database import db
from models.user import User
from flask_login import (
    LoginManager,
    login_user,
    current_user,
    logout_user,
    login_required,
)


app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:admin123@127.0.0.1:3306/flask-crud"
)
login_manager = LoginManager()

db.init_app(app)
login_manager.init_app(app)

login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            print(current_user.is_authenticated)
            return jsonify({"message": "Autenticação realizada com sucesso."})

    return jsonify({"message": "Credenciais inválidas."}), 400


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout realizado com sucesso."})


@app.route("/user", methods=["POST"])
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({"message": "Usuário já existe, escolha outro username."}), 403

    if username and password:
        user = User(username=username, password=password, role="user")
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "Usuário criado com suscesso."})

    return jsonify({"message": "Dados inválidos"}), 400


@app.route("/user/<int:user_id>", methods=["GET"])
@login_required
def get_user(user_id):
    user = User.query.get(user_id)

    if user:
        return jsonify({"username": f"{user.username}"})

    return jsonify({"message": "Usuário não encontrado."}), 404


@app.route("/users", methods=["GET"])
@login_required
def get_all_users():
    get_users = User.query.order_by(User.id).all()
    users_list = []

    for u in get_users:
        users_list.append({"id": int(u.id), "username": u.username})

    return jsonify({"message": f"{users_list}"})


@app.route("/user/<int:user_id>", methods=["PUT"])
@login_required
def update_user(user_id):
    user = User.query.get(user_id)
    data = request.json

    if user_id != current_user.id and current_user.role == "user":
        return jsonify({"message": "Operação não permitida."}), 403

    if user and data.get("password"):
        user.password = data.get("password")
        db.session.commit()

        return jsonify({"message": "Usuário atualizado com sucesso."})

    return jsonify({"message": "Usuário não encontrado."}), 404


@app.route("/user/<int:user_id>", methods=["DELETE"])
@login_required
def delete_user(user_id):
    user = User.query.get(user_id)

    if current_user.role != "admin":
        return jsonify({"message": "Operação não permitida."}), 403

    if user:
        if user_id == current_user.id:
            return jsonify({"message": "Não é possivel se auto remover."}), 403
        elif user.role == "admin":
            return jsonify({"message": "O usuário admin não pode ser deletado."}), 403
        elif user.role != "admin" and user_id != current_user.id:
            db.session.delete(user)
            db.session.commit()
            return jsonify({"message": f"Usuário {user.username} deletado com sucesso."})

    return jsonify({"message": "Usuário não encontrado."}), 404


if __name__ == "__main__":
    app.run(debug=True)
