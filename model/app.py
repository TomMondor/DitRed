from flask import Flask

app = Flask(__name__)


@app.route("/")
def start_page():
    return "<p>Welcome to DitRed<p>"


@app.route("/users", methods=["GET"])
def get_all_users():
    pass


@app.route("/users/:userId", methods=["GET"])
def get_user():
    pass


@app.route("/users/:userId", methods=["POST"])
def post_user():
    pass
