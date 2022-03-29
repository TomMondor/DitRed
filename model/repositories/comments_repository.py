from repositories.repository import Repository


class CommentsRepository(Repository):
    def __init__(self):
        super().__init__()

    def get_comments(self, sub_post_id):
        self.cursor.execute(f"SELECT * FROM Subpostcomments WHERE sub_post_id = {sub_post_id}")
        return self.cursor.fetchall()

    def get_comment(self, comment_id):
        self.cursor.execute(f"SELECT * FROM Subpostcomments WHERE id = {comment_id}")
        return self.cursor.fetchone()
