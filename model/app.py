from flask import Flask

app = Flask(__name__)


@app.route("/")
def start_page():
    return "<p>Welcome to DitRed<p>"


@app.route("/users", methods=["GET"])
def get_all_users():
    return "<p>all users<p>"


@app.route("/users/:userId", methods=["GET"])
def get_user():
    pass
