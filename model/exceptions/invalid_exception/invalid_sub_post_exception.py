from exceptions.invalid_exception.invalid_parameter_exception import InvalidParameterException


class InvalidSubPostIdException(InvalidParameterException):
    def __init__(self):
        super().__init__("Invalid sub post id")


class InvalidSubPostTitleException(InvalidParameterException):
    def __init__(self):
        super().__init__("Invalid sub post title")


class InvalidSubPostContentException(InvalidParameterException):
    def __init__(self):
        super().__init__("Invalid sub post content")

class InvalidSubPostVoteException(InvalidParameterException):
    def __init__(self):
        super().__init__("Invalid sub post vote")

class InvalidSubPostCommentIdException(InvalidParameterException):
    def __init__(self):
        super().__init__("Invalid sub post comment id")

class InvalidAnsweredCommentIdException(InvalidParameterException):
    def __init__(self):
        super().__init__("Invalid answered comment")
