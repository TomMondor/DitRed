from repositories.repository import Repository


class SubPostsRepository(Repository):
    def __init__(self):
        super().__init__()

    def get_posts(self, sub_id):
        self.cursor.execute(f"SELECT * FROM Subposts WHERE sub_id = '{sub_id}'")
        return self.cursor.fetchall()
