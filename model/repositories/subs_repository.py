from repositories.repository import Repository


class SubsRepository(Repository):
    def __init__(self):
        super().__init__()

    def get_subs(self):
        self.cursor.execute("SELECT * FROM Subs")
        return self.cursor.fetchall()

    def get_sub(self, id):
        self.cursor.execute(f"SELECT * FROM Subs WHERE id = {id}")
        return self.cursor.fetchone()

    def create_sub(self, name, creator_id, description):
        self.cursor.execute(f"INSERT INTO Subs (name, creator_id, timestamp, description, subscribers_count) " +
                            f"VALUES ('{name}', {creator_id}, NOW(), '{description}', 0)")
        return self.cursor.lastrowid
