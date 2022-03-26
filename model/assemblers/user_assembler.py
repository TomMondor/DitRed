from exceptions.missing_exception.missing_user_exception import MissingUserException
from exceptions.missing_exception.missing_wall_post_exception import MissingWallPostException
from exceptions.invalid_exception.invalid_user_exception import *
import re


class UserAssembler:
    def __parse_user(self, user):
        user_info = {
            'email': user[1],
            'username': user[2],
            'bio': user[3],
            'age': user[4]
        }

        return user[0], user_info  # user[0] = user_id

    def assemble_users(self, users_list):
        users = {}
        for user in users_list:
            user_id, user_info = self.__parse_user(user)
            users[user_id] = user_info
        return users

    def assemble_user(self, user, wall_posts):
        user_id, user_info = self.__parse_user(user)
        user_info['wallPosts'] = wall_posts
        return {user_id: user_info}

    def check_create_wallpost_request(self, request):
        if request is None or 'wallPostContent' not in request:
            raise MissingWallPostException()
        wall_post_content = request["wallPostContent"]
        if wall_post_content is None:
            raise MissingWallPostException()
        if not isinstance(wall_post_content, str):
            raise InvalidWallPostException()

    def check_create_user_request(self, request):
        self.__check_request_fields_present(request)
        self.__check_user_email(request['email'])
        self.__check_user_username(request['username'])
        self.__check_user_bio(request['bio'])
        self.__check_user_age(request['age'])
        self.__check_user_password(request['password'])

    def __check_request_fields_present(self, request):
        if not request:
            raise MissingUserException()
        if 'email' not in request or 'username' not in request or 'bio' not in request \
                or 'age' not in request or 'password' not in request:
            raise MissingUserException()
        if request['email'] is None or request['username'] is None or request['bio'] is None \
                or request['age'] is None or request['password'] is None:
            raise MissingUserException()

    def __check_user_email(self, email):
        if len(email) > 256:
            raise InvalidEmailException()
        if not re.match(r'^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$', str(email)):
            raise InvalidEmailException()

    def __check_user_username(self, username):
        if len(username) > 30:
            raise InvalidUsernameException()

    def __check_user_bio(self, bio):
        if len(bio) > 1000:
            raise InvalidBioException()

    def __check_user_age(self, age):
        if isinstance(age, str):
            if not age.isdecimal() or int(age) < 0 or int(age) > 120:
                raise InvalidAgeException()
        elif isinstance(age, int):
            if age < 0 or age > 120:
                raise InvalidAgeException()
        else:
            raise InvalidAgeException()

    def __check_user_password(self, password):
        if not re.match(r'^[0-9a-f]{96}$', str(password)):
            raise InvalidPasswordException()
