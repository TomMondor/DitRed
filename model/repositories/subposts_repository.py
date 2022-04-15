from repositories.repository import Repository


class SubPostsRepository(Repository):
    def __init__(self):
        super().__init__()

    def get_posts(self, sub_id):
        self.cursor.execute(
            f"SELECT S.*, U.username FROM SubPosts S, Users U WHERE S.sub_id = %s AND S.creator_id = U.id",
            (sub_id,))
        return self.cursor.fetchall()

    def get_post(self, post_id):
        self.cursor.execute(
            f"SELECT S.*, U.username FROM SubPosts S, Users U WHERE S.id = %s AND S.creator_id = U.id",
            (post_id,))
        return self.cursor.fetchone()

    def create_post(self, sub_id, title, content, creator_id):
        self.cursor.execute(
            f"INSERT INTO Subposts (sub_id, creator_id, timestamp, title, content, score, comments_count)" +
            f" VALUES (%s, %s, NOW(), %s, %s, 0, 0)", (sub_id, creator_id, title, content)
        )
        return self.cursor.lastrowid

    def create_vote(self, sub_post_id, voter_id, vote):
        self.cursor.execute(
            f"INSERT INTO SubPostsVotes (sub_post_id, user_id, vote)" +
            f" VALUES (%s, %s, %s)", (sub_post_id, voter_id, vote)
        )

    def get_subbed_posts(self, user_id):
        self.cursor.execute(f"SELECT SP.*, SB.name, U.username "
                            f"FROM SubPosts SP, Subscribers S, Users U, Subs SB "
                            f"WHERE S.user_id = %s AND S.sub_id = SP.sub_id "
                            f"AND SP.creator_id = U.id AND SP.sub_id = SB.id",
                            (user_id,))

        return self.cursor.fetchall()
