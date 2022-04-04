from uuid import uuid4


class LoginTokensRepository:
    def __init__(self):
        self.login_tokens = {}

    def create_login_token(self, user_id):
        login_token = str(uuid4())
        self.login_tokens[user_id] = login_token
        return login_token

    def validate_login_token(self, user_id, login_token):
        if user_id not in self.login_tokens.keys():
            return False
        return self.login_tokens[user_id] == login_token
