from repositories.repository import Repository


class CommentsRepository(Repository):
    def __init__(self):
        super().__init__()

    def get_comments(self, sub_post_id):
        self.cursor.execute(f"SELECT * FROM SubPostComments WHERE sub_post_id = {sub_post_id}")
        return self.cursor.fetchall()

    def get_comment(self, comment_id):
        self.cursor.execute(f"SELECT * FROM SubPostComments WHERE id = {comment_id}")
        return self.cursor.fetchone()

    def create_comment(self, sub_post_id, user_id, comment):
        self.cursor.execute(
            f"INSERT INTO SubPostComments (sub_post_id, user_id, timestamp, comment, score, answered_comment_id)" +
            f" VALUES ({sub_post_id}, {user_id}, NOW(), '{comment}', 0, NULL)"
        )

        return self.cursor.lastrowid

    def create_comment_answer(self, sub_post_id, comment_id, user_id, comment):
        self.cursor.execute(
            f"INSERT INTO SubPostComments (sub_post_id, user_id, timestamp, comment, score, answered_comment_id)" +
            f" VALUES ({sub_post_id}, {user_id}, NOW(), '{comment}', 0, {comment_id})"
        )

        return self.cursor.lastrowid

    def create_vote(self, comment_id, user_id, vote):
        self.cursor.execute(
            f"INSERT INTO SubPostCommentsVotes (sub_post_comment_id, user_id, vote)" +
            f" VALUES ({comment_id}, {user_id}, '{vote}')"
        )
