class InvalidParameterException(Exception):
    def __init__(self, message):
        self.status_code = 404
        self.message = message
