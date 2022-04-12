from repositories.repository import Repository
from datetime import datetime


class MessagesRepository(Repository):
    def __init__(self):
        super().__init__()

    def get_convos(self, id):
        self.cursor.execute(
            f"SELECT DISTINCT sender_id, (SELECT username FROM Users WHERE id = sender_id) FROM Messages WHERE receiver_id = %s\
                UNION\
                SELECT DISTINCT receiver_id, (SELECT username FROM Users WHERE id = receiver_id) FROM Messages WHERE sender_id = %s",
            (id, id)
        )
        return self.cursor.fetchall()

    def get_convo(self, first_user_id, second_user_id):
        self.cursor.execute(
            f"SELECT * FROM Messages WHERE sender_id = %s AND receiver_id = %s\
                UNION\
                SELECT * FROM Messages WHERE sender_id = %s AND receiver_id = %s",
            (first_user_id, second_user_id, second_user_id, first_user_id)
        )
        return self.cursor.fetchall()

    def create_message(self, sender_id, receiver_id, content):
        timestamp = datetime.today()
        self.cursor.execute(
            f"INSERT INTO Messages (sender_id, receiver_id, timestamp, message)\
                VALUES (%s, %s, %s, %s);",
            (sender_id, receiver_id, timestamp, content)
        )
        self.cursor.execute(
            f"SELECT LAST_INSERT_ID();"
        )
        id = self.cursor.fetchall()
        return id, sender_id, receiver_id, timestamp, content
