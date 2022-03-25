from exceptions.invalid_exception.invalid_parameter_exception import InvalidParameterException


class InvalidUserException(InvalidParameterException):
    def __init__(self):
        super().__init__("Invalid user id")
