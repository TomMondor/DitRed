class CommentAssembler:
    def __parse_comment(self, comment):
        return {
            'id': comment[0],
            'sub_post_id': comment[1],
            'creator_id': comment[2],
            'creator_name': comment[7],
            'timestamp': comment[3],
            'comment': comment[4],
            'score': comment[5],
            'answers_to': comment[6]
        }

    def assemble_comments(self, comments):
        post_comments = {}
        for comment in comments:
            comment_id = comment[0]
            post_comments[comment_id] = self.__parse_comment(comment)
        return post_comments
