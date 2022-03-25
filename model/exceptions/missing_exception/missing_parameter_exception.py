class MissingParameterException(Exception):
    def __init__(self, message):
        self.status_code = 400
        self.message = message
