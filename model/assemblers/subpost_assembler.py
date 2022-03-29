class SubPostAssembler:
    def assemble_posts(self, posts, authors):
        sub_posts = {}
        for post in posts:
            sub_post_id = post[0]
            sub_posts[sub_post_id] = {
                'sub_id': post[1],
                'creator_id': post[2],
                'creator_name': authors[post[2]],
                'timestamp': post[3],
                'title': post[4],
                'content': post[5],
                'score': post[6],
                'comments_count': post[7],
            }
        return sub_posts
