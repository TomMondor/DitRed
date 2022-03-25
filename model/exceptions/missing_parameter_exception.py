class MissingParameterException(Exception):
    def __init__(self):
        self.status_code = 404
        self.detail = 'Invalid parameters'
