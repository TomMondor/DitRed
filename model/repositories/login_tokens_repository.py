from uuid import uuid4

class LoginTokensRepository():
    def __init__(self):
        self.login_tokens = []

    def create_login_token(self, userId):
        login_token = uuid4()
        self.login_tokens.append({userId: login_token})
        return login_token
