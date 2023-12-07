'''
brands_exception.py

This file contains custom exception classes for handling brand-related errors.

Each exception class is derived from the built-in Exception class and has a custom message attribute that describes the error. 
The __str__ method is overridden to return this custom message when the exception is converted to a string.
'''

class BrandsNotFoundError(Exception):
    '''
    Raised when no brands are found in the database.
    '''
    message = "Brands not found"

    def __str__(self) -> str:
        return self.message

class BrandNotFoundError(Exception):
    '''
    Raised when a specific brand is not found in the database.
    '''
    message = "Brand not found"

    def __str__(self) -> str:
        return self.message
    
class BrandAlreadyExistsError(Exception):
    '''
    Raised when attempting to create a brand that already exists in the database.
    '''
    message = "Brand already exists"

    def __str__(self) -> str:
        return self.message
    
class BrandNotCreatedError(Exception):
    '''
    Raised when a brand is not created in the database.
    '''
    message = "Brand not created"

    def __str__(self) -> str:
        return self.message