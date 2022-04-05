from exceptions.missing_exception.missing_parameter_exception import MissingParameterException


class MissingSubPostException(MissingParameterException):
    def __init__(self):
        super().__init__("Missing fields in sub post")

class MissingSubPostVoteException(MissingParameterException):
    def __init__(self):
        super().__init__("Missing fields in sub post vote")

class MissingSubPostCommentException(MissingParameterException):
    def __init__(self):
        super().__init__("Missing fields in sub post comment")
