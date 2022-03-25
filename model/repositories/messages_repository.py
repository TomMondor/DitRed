from repositories.repository import Repository


class MessagesRepository(Repository):
    def __init__(self):
        super().__init__()

    def get_convo(self, id):
        self.cursor.execute(
            f"SELECT DISTINCT sender_id, (SELECT username FROM Users WHERE id = sender_id) FROM Messages WHERE receiver_id = {id}\
                UNION\
                SELECT DISTINCT receiver_id, (SELECT username FROM Users WHERE id = receiver_id) FROM Messages WHERE sender_id = {id}"
        )
        return self.cursor.fetchall()
