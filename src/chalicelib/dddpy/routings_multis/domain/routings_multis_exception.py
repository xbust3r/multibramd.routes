
class RoutingsMultisNotFoundError(Exception):
    """
    Exception raised when routings multis are not found.
    """
    message = "Routings Multis Not Found Error"
    
    def __str__(self):
        return self.message
    
    
class RoutingMultiNotFoundError(Exception):
    """
    Exception raised when a routing multi is not found.
    """
    message = "Routing Multi Not Found Error"
    
    def __str__(self):
        return self.message
    
class RoutingMultiAlreadyExistsError(Exception):
    """
    Exception raised when a routing multi already exists.
    """
    message = "Routing Multi Already Exists Error"
    
    def __str__(self):
        return self.message