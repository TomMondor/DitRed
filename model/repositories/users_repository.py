from repositories.repository import Repository


class UsersRepository(Repository):
    def __init__(self):
        super().__init__()

    def get_users(self):
        self.cursor.execute("SELECT * FROM Users")
        return self.cursor.fetchall()

    def get_user(self, id):
        self.cursor.execute(f"SELECT * FROM Users WHERE id = {id}")
        return self.cursor.fetchone()
