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
        if 'email' not in request or 'username' not in request or 'bio' not in request or 'age' not in request:
            return False
        return True