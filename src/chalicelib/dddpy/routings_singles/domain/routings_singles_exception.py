
class SinglesRoutingsNotFoundError(Exception):
    """
    Exception raised when Singles Routings is empty.
    """
    message = "Singles Routings is empty"
    
    def __str__(self):
        return self.message


class SingleRoutingNotFoundError(Exception):
    """
    Exception raised when Single Routing is not found.
    """
    message = "Single Routing Not Found"
    
    def __str__(self):
        return self.message

    
class SingleRoutingAlreadyExistsError(Exception):
    """
    Exception raised when Single Routing already exists.
    """
    message = "Single Routing Already Exists"
    
    def __str__(self):
        return self.message