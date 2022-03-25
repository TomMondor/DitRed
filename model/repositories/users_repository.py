from repositories.repository import Repository


class UsersRepository(Repository):
    def __init__(self):
        super().__init__()

    def get_users(self):
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()