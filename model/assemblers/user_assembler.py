from exceptions.missing_exception.missing_user_exception import MissingUserException
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

    def assemble_user(self, user):
        user_id, user_info = self.__parse_user(user)
        return {user_id: user_info}

    def check_create_user_request(self, request):
        if not request:
            raise MissingUserException()
        if 'email' not in request or 'username' not in request or 'bio' not in request \
                or 'age' not in request or 'password' not in request:
            raise MissingUserException()
        if not re.match(r'^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$', str(request['email'])):
            raise InvalidEmailException()
        if isinstance(request['age'], str):
            if not request['age'].isdecimal() or int(request['age']) < 0 or int(request['age']) > 120:
                raise InvalidAgeException()
        elif isinstance(request['age'], int):
            if request['age'] < 0 or request['age'] > 120:
                raise InvalidAgeException()
        else:
            raise InvalidAgeException()
        if not re.match(r'^[0-9a-f]{96}$', str(request['password'])):
            raise InvalidPasswordException()
