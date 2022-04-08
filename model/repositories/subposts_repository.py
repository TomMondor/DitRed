from repositories.repository import Repository


class SubPostsRepository(Repository):
    def __init__(self):
        super().__init__()

    def get_posts(self, sub_id):
        self.cursor.execute(f"SELECT * FROM SubPosts WHERE sub_id = '{sub_id}'")
        return self.cursor.fetchall()

    def get_post(self, post_id):
        self.cursor.execute(f"SELECT * FROM SubPosts WHERE id = '{post_id}'")
        return self.cursor.fetchone()

    def create_post(self, sub_id, title, content, creator_id):
        self.cursor.execute(
            f"INSERT INTO Subposts (sub_id, creator_id, timestamp, title, content, score, comments_count)" +
            f" VALUES ({sub_id}, {creator_id}, NOW(), '{title}', '{content}', 0, 0)"
        )
        return self.cursor.lastrowid

    def create_vote(self, sub_post_id, voter_id, vote):
        self.cursor.execute(
            f"INSERT INTO SubPostsVotes (sub_post_id, user_id, vote)" +
            f" VALUES ({sub_post_id}, {voter_id}, '{vote}')"
        )
