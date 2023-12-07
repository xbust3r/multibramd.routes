
class LogsNotFoundError(Exception):
    """
    Exception raised when logs are not found.
    """
    message = "Logs not found"

    def __str__(self) -> str:
        return self.message

class LogNotFoundError(Exception):
    """
    Exception raised when a log is not found.
    """
    message = "Log not found"

    def __str__(self) -> str:
        return self.message
    
class LogAlreadyExistsError(Exception):
    """
    Exception raised when a log already exists.
    """
    message = "Log already exists"

    def __str__(self) -> str:
        return self.message
    
class LogNotCreatedError(Exception):
    """
    Exception raised when a log is not created.
    """
    message = "Log not created"

    def __str__(self) -> str:
        return self.message
