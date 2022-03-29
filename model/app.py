from flask import Flask, jsonify, request

from repositories.messages_repository import MessagesRepository
from repositories.users_repository import UsersRepository
from repositories.subs_repository import SubsRepository

from assemblers.message_assembler import MessageAssembler
from assemblers.user_assembler import UserAssembler
from assemblers.sub_assembler import SubAssembler

from exceptions.invalid_exception.invalid_parameter_exception import InvalidParameterException
from exceptions.invalid_exception.invalid_user_exception import InvalidUserIdException
from exceptions.invalid_exception.invalid_sub_exception import InvalidSubIdException
from exceptions.missing_exception.missing_parameter_exception import MissingParameterException

app = Flask(__name__)

users_repository = UsersRepository()
user_assembler = UserAssembler()

subs_repository = SubsRepository()
sub_assembler = SubAssembler()

messages_repository = MessagesRepository()
messages_assembler = MessageAssembler()


@app.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:8080"

    return response


@app.errorhandler(InvalidParameterException)
def handle_exception(e):
    response = jsonify({"message": e.message})

    return response, e.status_code


@app.errorhandler(MissingParameterException)
def handle_exception(e):
    response = jsonify({"message": e.message})

    return response, e.status_code


@app.route("/")  # TODO remove (or replace by sending frontend files)
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
    wall_posts = users_repository.get_wallposts(user_id)
    response = jsonify(user_assembler.assemble_user(user, wall_posts))

    return response


@app.route("/users", methods=["POST"])
def post_user():
    user_info = request.get_json()
    user_assembler.check_create_user_request(user_info)
    user_id = users_repository.create_user(user_info)
    response = jsonify({"userId": user_id})

    return response, 201


@app.route("/users/<int:user_id>", methods=["POST"])
def post_wall_post(user_id):
    # TODO check user token
    content = request.get_json()
    user_assembler.check_create_wallpost_request(content)
    wall_post_content = content["wallPostContent"]
    wall_post_id = users_repository.create_wallpost(user_id, wall_post_content)

    return {"wall_post_id": wall_post_id}, 201


@app.route("/subs", methods=["GET"])
def get_subs():
    subs = subs_repository.get_subs()
    response = jsonify(sub_assembler.assemble_subs(subs))

    return response


@app.route("/subs/<sub_id>", methods=["GET"])
def get_sub(sub_id):
    sub = subs_repository.get_sub(sub_id)
    if sub is None:
        raise InvalidSubIdException()
    response = jsonify(sub_assembler.assemble_sub(sub))

    return response


@app.route("/subs", methods=["POST"])
def post_sub():
    content = request.get_json()
    sub_assembler.check_create_sub_request(content)
    sub_id = subs_repository.create_sub(content["name"], content["creator_id"], content["description"])

    return {"sub_id": sub_id}, 201


@app.route("/subs/<sub_id>", methods=["PUT"])
def put_sub(sub_id):
    content = request.get_json()
    sub_assembler.check_create_sub_request(content)
    updated_sub_content = subs_repository.update_sub(
        sub_id,
        content["name"],
        content["creator_id"],
        content["description"]
    )

    return jsonify(sub_assembler.assemble_sub(updated_sub_content))


# TODO Implement token validation so random people can't get anyone's messages
@app.route("/convo", methods=["GET"])
def get_convo():
    id = request.headers.get("user_id")
    users = messages_repository.get_convos(id)
    response = jsonify(messages_assembler.assemble_users(users))

    return response


# TODO Implement token validation so random people can't get anyone's messages
@app.route("/convo/<user_id>", methods=["GET"])
def get_specific_convo(user_id):
    current_id = request.headers.get("user_id")
    convo = messages_repository.get_convo(current_id, user_id)
    response = jsonify(messages_assembler.assemble_convo(convo))

    return response


# TODO Implement token validation so random people can't get anyone's messages
@app.route("/convo/<user_id>", methods=["POST"])
def post_message(user_id):
    current_id = request.headers.get("user_id")
    req = request.get_json()
    content = req["content"]
    message = messages_repository.create_message(current_id, user_id, content)
    response = jsonify(messages_assembler.assemble_message(message))

    return response, 201


if __name__ == '__main__':
    app.run()
