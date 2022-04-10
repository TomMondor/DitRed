from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit

from repositories.messages_repository import MessagesRepository
from repositories.users_repository import UsersRepository
from repositories.subs_repository import SubsRepository
from repositories.subposts_repository import SubPostsRepository
from repositories.comments_repository import CommentsRepository
from repositories.login_tokens_repository import LoginTokensRepository
from repositories.chat_ids_repository import ChatIdsRepository

from assemblers.message_assembler import MessageAssembler
from assemblers.user_assembler import UserAssembler
from assemblers.sub_assembler import SubAssembler
from assemblers.subpost_assembler import SubPostAssembler
from assemblers.comment_assembler import CommentAssembler
from assemblers.validate_assembler import ValidateAssembler
from assemblers.subbedposts_assembler import SubbedPostsAssembler

from exceptions.invalid_exception.invalid_parameter_exception import InvalidParameterException
from exceptions.invalid_exception.invalid_user_exception import InvalidUserIdException
from exceptions.invalid_exception.invalid_sub_exception import InvalidSubIdException
from exceptions.invalid_exception.invalid_sub_post_exception import InvalidSubPostCommentIdException, InvalidSubPostIdException
from exceptions.invalid_exception.invalid_sub_post_exception import InvalidAnsweredCommentIdException
from exceptions.missing_exception.missing_parameter_exception import MissingParameterException

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

users_repository = UsersRepository()
user_assembler = UserAssembler()

subs_repository = SubsRepository()
sub_assembler = SubAssembler()

sub_posts_repository = SubPostsRepository()
sub_post_assembler = SubPostAssembler()
subbed_posts_assembler = SubbedPostsAssembler()

comments_repository = CommentsRepository()
comments_assembler = CommentAssembler()

messages_repository = MessagesRepository()
messages_assembler = MessageAssembler()

login_tokens_repository = LoginTokensRepository()
validate_assembler = ValidateAssembler()

chat_ids_repository = ChatIdsRepository()


@app.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:8080"
    response.headers["Access-Control-Allow-Headers"] = "userId,loginToken,content-type"

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


@app.route("/login", methods=["POST"])
def login():
    user_info = request.get_json()
    user_id = users_repository.verify_login(user_info)
    token = login_tokens_repository.create_login_token(user_id)
    response = jsonify({"token": token, "user_id": user_id})

    return response


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


@app.route("/users/usernames", methods=["GET"])
def get_usernames():
    username_substring = request.args.get("username", type=str)
    usernames = UsersRepository().get_matching_usernames(username_substring)
    if usernames is None:
        usernames = []
    response = jsonify(user_assembler.assemble_usernames(usernames))

    return response


@app.route("/usernames/<string:username>", methods=["GET"])
def get_user_by_username(username):
    user = UsersRepository().get_user_by_username(username)
    if user is None:
        raise InvalidUserIdException()
    wall_posts = users_repository.get_wallposts(user[0])
    response = jsonify(user_assembler.assemble_user(user, wall_posts))

    return response


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
    authors = {}
    for sub in subs:
        user_id = sub[2]
        authors[user_id] = users_repository.get_username(user_id)
    response = jsonify(sub_assembler.assemble_subs(subs, authors))

    return response


@app.route("/subs/<int:sub_id>", methods=["GET"])
def get_sub(sub_id):
    sub = subs_repository.get_sub(sub_id)
    if sub is None:
        raise InvalidSubIdException()
    author = UsersRepository().get_username(sub[2])
    response = jsonify(sub_assembler.assemble_sub(sub, author))

    return response


@app.route("/subs/<int:sub_id>/posts", methods=["GET"])
def get_sub_posts(sub_id):
    posts = sub_posts_repository.get_posts(sub_id)
    authors = {}
    for post in posts:
        user_id = post[2]
        authors[user_id] = UsersRepository().get_username(user_id)
    response = jsonify(sub_post_assembler.assemble_posts(posts, authors))

    return response


@app.route("/subs/<int:sub_id>/posts/<int:sub_post_id>", methods=["GET"])
def get_sub_post(sub_id, sub_post_id):
    post = sub_posts_repository.get_post(sub_post_id)
    if post is None:
        raise InvalidSubPostIdException()
    user_id = post[2]
    author = users_repository.get_username(user_id)
    comments = comments_repository.get_comments(sub_post_id)
    authors = {}
    for comment in comments:
        comment_id = comment[0]
        user_id = comment[2]
        authors[comment_id] = users_repository.get_username(user_id)
    assembled_comments = comments_assembler.assemble_comments(comments, authors)
    response = jsonify(sub_post_assembler.assemble_post(post, author, assembled_comments))

    return response


@app.route("/subs", methods=["POST"])
def post_sub():
    content = request.get_json()
    sub_assembler.check_create_sub_request(content)
    sub_id = subs_repository.create_sub(content["name"], content["creator_id"], content["description"])

    return {"sub_id": sub_id}, 201


@app.route("/subs/<int:sub_id>", methods=["PUT"])
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


# TODO Implement token validation
@app.route("/subs/<int:sub_id>/posts", methods=["POST"])
def post_sub_post(sub_id):
    content = request.get_json()
    sub_post_assembler.check_create_sub_post_request(content)

    creator = users_repository.get_user(content["creator_id"])
    sub = subs_repository.get_sub(sub_id)
    if creator is None:
        raise InvalidUserIdException()
    if sub is None:
        raise InvalidSubIdException()
    sub_post_id = sub_posts_repository.create_post(sub_id, content["title"], content["content"], content["creator_id"])

    return {"sub_post_id": sub_post_id}, 201

#TODO Implement token validation
@app.route("/subs/<int:sub_id>/posts/<int:sub_post_id>/vote", methods=["POST"])
def post_sub_post_vote(sub_id, sub_post_id):
    content = request.get_json()
    print(content)
    sub_post_assembler.check_vote_request(content)

    voter = users_repository.get_user(content["voter_id"])
    sub_post = sub_posts_repository.get_post(sub_post_id)
    if voter is None:
        print("pog")
        raise InvalidUserIdException()
    if sub_post is None:
        print("pag")
        raise InvalidSubPostIdException()
    sub_posts_repository.create_vote(sub_post_id, content["voter_id"], content["vote"])

    return {}, 201


#TODO Implement token validation
@app.route("/subs/<int:sub_id>/posts/<int:sub_post_id>/comments", methods=["POST"])
def post_sub_post_comment(sub_id, sub_post_id):
    content = request.get_json()
    sub_post_assembler.check_comment_sub_post_request(content)

    creator = users_repository.get_user(content["user_id"])
    sub_post = sub_posts_repository.get_post(sub_post_id)
    if creator is None:
        raise InvalidUserIdException()
    if sub_post is None:
        raise InvalidSubPostIdException()
    comment_id = comments_repository.create_comment(sub_post_id, content["user_id"], content["comment"])

    return {"sub_post_comment_id": comment_id}, 201


#TODO Implement token validation
@app.route("/subs/<int:sub_id>/posts/<int:sub_post_id>/comments/<int:comment_id>", methods=["POST"])
def post_sub_post_comment_answer(sub_id, sub_post_id, comment_id):
    content = request.get_json()
    sub_post_assembler.check_comment_sub_post_request(content)

    creator = users_repository.get_user(content["user_id"])
    sub_post = sub_posts_repository.get_post(sub_post_id)
    original_comment = comments_repository.get_comment(comment_id)
    if creator is None:
        raise InvalidUserIdException()
    if sub_post is None:
        raise InvalidSubPostIdException()
    if original_comment is None:
        raise InvalidAnsweredCommentIdException()
    comment_id = comments_repository.create_comment_answer(sub_post_id, comment_id, content["user_id"], content["comment"])

    return {"sub_post_comment_id": comment_id}, 201


#TODO Implement token validation
@app.route("/subs/<int:sub_id>/posts/<int:sub_post_id>/comments/<int:comment_id>/vote", methods=["POST"])
def post_sub_post_comment_vote(sub_id, sub_post_id, comment_id):
    content = request.get_json()
    sub_post_assembler.check_vote_request(content)

    creator = users_repository.get_user(content["voter_id"])
    sub_post = sub_posts_repository.get_post(sub_post_id)
    comment = comments_repository.get_comment(comment_id)
    if creator is None:
        raise InvalidUserIdException()
    if sub_post is None:
        raise InvalidSubPostIdException()
    if comment is None:
        raise InvalidSubPostCommentIdException()
    comments_repository.create_vote(comment_id, content["voter_id"], content["vote"])

    return {}, 201


#TODO Implement token validation
@app.route("/subs/<int:sub_id>/subscribe", methods=["POST"])
def post_sub_subscription(sub_id):
    content = request.get_json()
    sub_assembler.check_subscribe_request(content)
    sub = subs_repository.get_sub(sub_id)
    if sub is None:
        raise InvalidSubIdException()
    subs_repository.create_subscription(content["user_id"], sub_id)

    return {}, 201


# TODO Implement token validation so random people can't get anyone's messages
@app.route("/convo", methods=["GET"])
def get_convo():
    id = request.headers.get("userId")
    users = messages_repository.get_convos(id)
    response = jsonify(messages_assembler.assemble_users(users))

    return response


# TODO Implement token validation so random people can't get anyone's messages
@app.route("/convo/<int:user_id>", methods=["GET"])
def get_specific_convo(user_id):
    current_id = request.headers.get("userId")
    convo = messages_repository.get_convo(current_id, user_id)
    response = jsonify(messages_assembler.assemble_convo(convo))

    return response


# TODO Implement token validation so random people can't get anyone's messages
@app.route("/convo/<int:user_id>", methods=["POST"])
def post_message(user_id):
    current_id = request.headers.get("userId")
    req = request.get_json()
    content = req["message"]
    message = messages_repository.create_message(current_id, user_id, content)
    response = jsonify(messages_assembler.assemble_message(message))

    return response, 201


@app.route("/subbed", methods=["GET"])
def get_subbed_posts():
    current_id = request.headers.get("userId")
    subbed_posts = sub_posts_repository.get_subbed_posts(current_id)

    authors = {}
    sub_names = {}
    for post in subbed_posts:
        user_id = post[2]
        authors[user_id] = UsersRepository().get_username(user_id)
        sub_names[user_id] = SubsRepository().get_sub_name(post[1])
    response = jsonify(subbed_posts_assembler.assemble_subbed_posts(subbed_posts, authors, sub_names))

    return response


@app.route("/validate", methods=["GET"])
def validate_user():
    user_id = request.headers.get("userId")
    login_token = request.headers.get("loginToken")
    response = jsonify(validate_assembler.assemble_validation(user_id, login_token, login_tokens_repository))
    return response


@socketio.on('message from user', namespace='messages')
def receive_message_from_user(message):
    print(f'USER MESSAGE: {message}')
    emit('user message', message, broadcast=True)


@socketio.on('user_id', namespace='/private')
def receive_user_id(user_id):
    chat_ids_repository.add_user_chat_id(user_id, request.sid)


@socketio.on('private_message', namespace='/private')
def private_message(payload):
    my_user_id = payload['myUserId']
    user_id = payload["userId"]
    message = payload["message"]
    if user_id in chat_ids_repository.get_chat_ids_keys():
        emit('new_private_message', {my_user_id: message}, room=chat_ids_repository.get_chat_id_by_user_id(user_id))


if __name__ == '__main__':
    socketio.run(app)
