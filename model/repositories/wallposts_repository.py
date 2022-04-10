from repositories.repository import Repository


class WallPostsRepository(Repository):
    def __init__(self):
        super().__init__()

    def get_subbed_posts(self, user_id):
        self.cursor.execute(f"SELECT * "
                            f"FROM SubPosts SP, Subscribers S "
                            f"WHERE S.user_id = '{user_id}' AND S.sub_id = SP.sub_id")

        return self.cursor.fetchall()
