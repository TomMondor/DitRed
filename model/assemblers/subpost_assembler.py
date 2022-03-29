class SubPostAssembler:
    def __parse_post(self, post, author):
        return {
            'sub_id': post[1],
            'creator_id': post[2],
            'creator_name': author,
            'timestamp': post[3],
            'title': post[4],
            'content': post[5],
            'score': post[6],
            'comments_count': post[7],
        }

    def assemble_posts(self, posts, authors):
        sub_posts = {}
        for post in posts:
            sub_post_id = post[0]
            sub_posts[sub_post_id] = self.__parse_post(post, authors[post[2]])
        return sub_posts

    def assemble_post(self, post, author, comments):
        post = self.__parse_post(post, author)
        post['comments'] = comments
        return post
