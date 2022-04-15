from exceptions.missing_exception.missing_sub_post_exception import *
from exceptions.invalid_exception.invalid_sub_post_exception import *
from exceptions.invalid_exception.invalid_user_exception import InvalidUserIdException


class SubbedPostsAssembler:
    def __parse_post(self, post):
        return {
            'sub_id': post[1],
            'creator_id': post[2],
            'creator_name': post[9],
            'timestamp': post[3],
            'title': post[4],
            'content': post[5],
            'score': post[6],
            'comments_count': post[7],
            'sub_name': post[8]
        }

    def assemble_subbed_posts(self, posts):
        sub_posts = {}
        for post in posts:
            sub_post_id = post[0]
            sub_posts[sub_post_id] = self.__parse_post(post)
        return sub_posts
