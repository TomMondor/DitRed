from uuid import uuid4


class ChatIdsRepository():
    def __init__(self):
        self.chat_ids = {}

    def add_user_chat_id(self, user_id, sid):
        self.chat_ids[user_id] = sid

    def get_chat_ids_keys(self):
        return self.chat_ids.keys()
