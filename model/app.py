from flask import Flask, jsonify, request
from repositories.users_repository import UsersRepository
from assemblers.user_assembler import UserAssembler
from exceptions.missing_parameter_exception import MissingParameterException

app = Flask(__name__)

users_repository = UsersRepository()
user_assembler = UserAssembler()


@app.route("/")
def start_page():
    return "<p>Welcome to DitRed<p>"


@app.route("/users", methods=["GET"])
def get_all_users():
    users = users_repository.get_users()
    response = jsonify(user_assembler.assemble_users(users))
    return response


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users_repository.get_user(user_id)
    if user is None:
        raise MissingParameterException()
    response = jsonify(user_assembler.assemble_user(user))
    return response


@app.route("/users/:userId", methods=["POST"])
def post_user():
    pass


@app.errorhandler(MissingParameterException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    response = jsonify({"message": e.detail})
    return response, e.status_code


if __name__ == '__main__':
    app.run()
