from flask import Flask, jsonify, request
from repositories.users_repository import UsersRepository
from assemblers.user_assembler import UserAssembler

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


@app.route("/users/:userId", methods=["GET"])
def get_user():
    pass


@app.route("/users/:userId", methods=["POST"])
def post_user():
    pass


if __name__ == '__main__':
    app.run()
