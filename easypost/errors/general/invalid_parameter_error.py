from easypost.errors.general.easypost_error import EasyPostError


class InvalidParameterError(EasyPostError):
    def __init__(self, message: str):
        super().__init__(message=message)
