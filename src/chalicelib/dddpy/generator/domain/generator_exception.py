
"""
This file contains custom exception classes for the generator domain.

- InvalidUrlException: Exception raised for invalid URLs.
- TypeNotSupportedException: Exception raised for unsupported types.
- GeneratorRoutesNotConfigured: Exception raised when no configuration is found with the given parameters.
"""

class InvalidUrlException(Exception):
    message = "Invalid URL"
    
    def __str__(self):
        return self.message
    
class TypeNotSupportedException(Exception):
    message = "Type not supported"
    
    def __str__(self):
        return self.message
    
class GeneratorRoutesNotConfigured(Exception):
    message = "we are not found any configuration with your params"
    
    def __str__(self) -> str:
        return self.message