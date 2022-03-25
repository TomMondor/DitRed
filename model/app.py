from flask import Flask, jsonify

from repositories.users_repository import UsersRepository
from repositories.subs_repository import SubsRepository

from assemblers.user_assembler import UserAssembler
from assemblers.sub_assembler import SubAssembler

from exceptions.invalid_exception.invalid_parameter_exception import InvalidParameterException
from exceptions.invalid_exception.invalid_user_exception import InvalidUserException
from exceptions.invalid_exception.invalid_sub_exception import InvalidSubException


app = Flask(__name__)

users_repository = UsersRepository()
user_assembler = UserAssembler()

subs_repository = SubsRepository()
sub_assembler = SubAssembler()


@app.errorhandler(InvalidParameterException)
def handle_exception(e):
    response = jsonify({"message": e.message})
    return response, e.status_code


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
        raise InvalidUserException()
    response = jsonify(user_assembler.assemble_user(user))
    return response


@app.route("/users/:userId", methods=["POST"])
def post_user():
    pass


@app.route("/subs", methods=["GET"])
def get_subs():
    subs = subs_repository.get_subs()
    response = jsonify(sub_assembler.assemble_subs(subs))
    return response


@app.route("/subs/<sub_id>", methods=["GET"])
def get_sub(sub_id):
    sub = subs_repository.get_sub(sub_id)
    if sub is None:
        raise InvalidSubException()
    response = jsonify(sub_assembler.assemble_sub(sub))
    return response


@app.route("/subs", methods=["POST"])
def post_sub():
    pass


if __name__ == '__main__':
    app.run()
