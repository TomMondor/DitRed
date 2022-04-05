from exceptions.missing_exception.missing_sub_post_exception import *
from exceptions.invalid_exception.invalid_sub_post_exception import *
from exceptions.invalid_exception.invalid_user_exception import InvalidUserIdException


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

    def check_create_sub_post_request(self, request):
        self.__check_request_exists(request)
        self.__check_request_parameters_not_empty(request)
        self.__check_parameters_types(request)
        self.__check_request_parameters_length(request)

    def check_vote_sub_post_request(self, request):
        self.__check_request_exists(request)
        self.__check_vote_request_parameters_not_empty(request)
        self.__check_vote_request_parameters_types(request)

    def check_comment_sub_post_request(self, request):
        self.__check_request_exists(request)
        self.__check_comment_request_parameters_not_empty(request)
        self.__check_comment_request_parameters_types(request)
        self.__check_comment_request_parameters_length(request)

    def __check_request_exists(self, request):
        if request is None:
            raise MissingSubPostException()

    def __check_request_parameters_not_empty(self, request):
        if "title" not in request or "content" not in request or "creator_id" not in request:
            raise MissingSubPostException()
        if request["title"] is None or request["content"] is None or request["creator_id"] is None:
            raise MissingSubPostException()

    def __check_vote_request_parameters_not_empty(self, request):
        if "vote" not in request or "voter_id" not in request:
            raise MissingSubPostVoteException()
        if request["vote"] is None or request["voter_id"] is None:
            raise MissingSubPostVoteException()

    def __check_comment_request_parameters_not_empty(self, request):
        if "user_id" not in request or "comment" not in request:
            raise MissingSubPostCommentException()
        if request["user_id"] is None or request["comment"] is None:
            raise MissingSubPostCommentException()

    def __check_request_parameters_length(self, request):
        if len(request["title"]) > 255 or len(request["title"]) < 1:
            raise InvalidSubPostTitleException()
        if len(request["content"]) < 1:
            raise InvalidSubPostContentException()

    def __check_comment_request_parameters_length(self, request):
        if len(request["comment"]) > 2999 or len(request["comment"]) < 1:
            raise InvalidSubPostCommentException()

    def __check_parameters_types(self, request):
        if not isinstance(request["title"], str):
            raise InvalidSubPostTitleException()
        if not isinstance(request["content"], str):
            raise InvalidSubPostContentException()
        if not isinstance(request["creator_id"], int):
            raise InvalidUserIdException()

    def __check_vote_request_parameters_types(self, request):
        if not isinstance(request["voter_id"], int):
            raise InvalidUserIdException()
        if not isinstance(request["vote"], str) :
            raise InvalidSubPostVoteException()

    def __check_comment_request_parameters_types(self, request):
        if not isinstance(request["user_id"], int):
            raise InvalidUserIdException()
        if not isinstance(request["comment"], str) :
            raise InvalidSubPostCommentException()
