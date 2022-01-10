class CustomBaseException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class CredentialKeysNotProvided(CustomBaseException):
    """
    Raised when one of the Required Keys is not provided
    """
    pass
