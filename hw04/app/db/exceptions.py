class UserNotFoundError(Exception):
    pass


class CRUDError(Exception):
    def __init__(self, message, e):
        """
        @param message: description
        @param e: error
        """
        self.msg = f"{message}: {e.__str__()}"
