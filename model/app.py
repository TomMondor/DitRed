from flask import Flask, jsonify
from repositories.users_repository import UsersRepository
from assemblers.user_assembler import UserAssembler
from repositories.subs_repository import SubsRepository
from assemblers.sub_assembler import SubAssembler

app = Flask(__name__)

users_repository = UsersRepository()
user_assembler = UserAssembler()

subs_repository = SubsRepository()
sub_assembler = SubAssembler()


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


@app.route("/subs", methods=["GET"])
def get_subs():
    subs = subs_repository.get_subs()
    response = jsonify(sub_assembler.assemble_subs(subs))
    return response


@app.route("/subs/<sub_id>", methods=["GET"])
def get_sub(sub_id):
    sub = subs_repository.get_sub(sub_id)
    response = jsonify(sub_assembler.assemble_sub(sub))
    return response


@app.route("/subs", methods=["POST"])
def post_sub():
    pass


if __name__ == '__main__':
    app.run()
