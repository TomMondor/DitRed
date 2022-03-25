class UserAssembler:
    def assemble_user(self, user):
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
            user_id, user_info = self.assemble_user(user)
            users[user_id] = user_info
        return users
