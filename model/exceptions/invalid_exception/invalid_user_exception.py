from exceptions.invalid_exception.invalid_parameter_exception import InvalidParameterException


class InvalidUserIdException(InvalidParameterException):
    def __init__(self):
        super().__init__("Invalid user id")
        self.status_code = 404


class InvalidUsernameException(InvalidParameterException):
    def __init__(self):
        super().__init__("Invalid username")


class InvalidPasswordException(InvalidParameterException):
    def __init__(self):
        super().__init__("Invalid user password")


class InvalidEmailException(InvalidParameterException):
    def __init__(self):
        super().__init__("Invalid user email")


class InvalidAgeException(InvalidParameterException):
    def __init__(self):
        super().__init__("Invalid user age")

class InvalidWallPostException(InvalidParameterException):
    def __init__(self):
        super().__init__("Invalid wall post content")
