class RoutingsMultisUrlsNotFoundError(Exception):
    """
    Exception raised when routings multis are not found.
    """

    message = "Routings Multis Not Found Error"

    def __str__(self):
        return self.message
    
    
class RoutingMultiUrlNotFoundError(Exception):
    message="Routing Multi Not Found Error"
    
    def __str__(self):
        return self.message
    
class RoutingMultiUrlAlreadyExistsError(Exception):
    message="Routing Multi Already Exists Error"
    
    def __str__(self):
        return self.message