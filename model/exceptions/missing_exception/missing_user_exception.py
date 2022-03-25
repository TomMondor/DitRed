from exceptions.missing_exception.missing_parameter_exception import MissingParameterException


class MissingUserException(MissingParameterException):
    def __init__(self):
        super().__init__("Missing fields in user")
