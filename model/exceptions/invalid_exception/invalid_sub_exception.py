from exceptions.invalid_exception.invalid_parameter_exception import InvalidParameterException


class InvalidSubException(InvalidParameterException):
    def __init__(self):
        super().__init__("Invalid sub id")
