class ConfigurationsNotFoundError(Exception):
    """
    Exception raised when configurations are not found.
    """

    message = "Configurations not found"

    def __str__(self):
        return self.message
    
class ConfigurationNotFoundError(Exception):
    message="Configuration not found"
    def __str__(self):
        return self.message
    
class ConfigurationAlreadyExistsError(Exception):
    message="Configuration already exists"
    def __str__(self):
        return self.message
    
class ConfigurationNotCreatedError(Exception):
    message="Configuration not created"
    def __str__(self):
        return self.message
    