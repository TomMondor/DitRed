from exceptions.missing_exception.missing_parameter_exception import MissingParameterException


class MissingWallPostException(MissingParameterException):
    def __init__(self):
        super().__init__("Missing wall post field")
