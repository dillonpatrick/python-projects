from flask import Flask, request, jsonify
app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"


@app.route("/hello", methods=["GET"])
def hello_world():
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)
