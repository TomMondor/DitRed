from flask import Flask, jsonify, request

from repositories.users_repository import UsersRepository
from repositories.subs_repository import SubsRepository

from assemblers.user_assembler import UserAssembler
from assemblers.sub_assembler import SubAssembler

from exceptions.invalid_exception.invalid_parameter_exception import InvalidParameterException
from exceptions.invalid_exception.invalid_user_exception import InvalidUserIdException
from exceptions.invalid_exception.invalid_sub_exception import InvalidSubException
from exceptions.missing_exception.missing_parameter_exception import MissingParameterException


app = Flask(__name__)

users_repository = UsersRepository()
user_assembler = UserAssembler()

subs_repository = SubsRepository()
sub_assembler = SubAssembler()


@app.errorhandler(InvalidParameterException)
def handle_exception(e):
    response = jsonify({"message": e.message})
    return response, e.status_code


@app.errorhandler(MissingParameterException)
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
        raise InvalidUserIdException()
    response = jsonify(user_assembler.assemble_user(user))
    return response


@app.route("/users", methods=["POST"])
def post_user():
    user_info = request.get_json()
    user_assembler.check_create_user_request(user_info)
    user_id = users_repository.create_user(user_info)
    response = jsonify({"userId": user_id})
    return response, 201


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
    content = request.get_json()
    sub_id = subs_repository.create_sub(content["name"], content["creator_id"], content["description"])
    return {"sub_id": sub_id}


if __name__ == '__main__':
    app.run()
