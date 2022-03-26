from exceptions.invalid_exception.invalid_parameter_exception import InvalidParameterException


class InvalidSubIdException(InvalidParameterException):
    def __init__(self):
        super().__init__("Invalid sub id")


class InvalidSubNameException(InvalidParameterException):
    def __init__(self):
        super().__init__("Invalid sub name")


class InvalidSubDescriptionException(InvalidParameterException):
    def __init__(self):
        super().__init__("Invalid sub description")


class InvalidSubCreatorIdException(InvalidParameterException):
    def __init__(self):
        super().__init__("Invalid sub creator id")
