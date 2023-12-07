'''
brands_repository.py

This file defines the interface for brand-related database operations.

It imports the necessary Pydantic models for handling brand data, including the CreateBrandSchema and UpdateBrandSchema.

The BrandRepository class is an interface for brand-related database operations. It defines methods for getting all brands, 
finding a brand by id or code, and creating or updating a brand. Each method raises a NotImplementedError, indicating that 
it must be implemented by any class that inherits from BrandRepository.
'''

from chalicelib.dddpy.brands.usecase.brands_cmd_schema import (
    CreateBrandSchema,
    UpdateBrandSchema,
)

class BrandRepository:
    '''
    The BrandRepository class is an interface for brand-related database operations. 
    It defines methods for getting all brands, finding a brand by id or code, and creating or updating a brand. 
    Each method raises a NotImplementedError, indicating that it must be implemented by any class that inherits from BrandRepository.
    '''

    def all(self):
        '''
        This method should return all brands.
        '''
        raise NotImplementedError

    def find_by_id(self, id: int):
        '''
        This method should find and return a brand by its id.
        '''
        raise NotImplementedError

    def find_by_code(self, code: str):
        '''
        This method should find and return a brand by its code.
        '''
        raise NotImplementedError

    def create(self, data: CreateBrandSchema):
        '''
        This method should create a new brand.
        It takes a CreateBrandSchema object as input, which represents the data for the new brand.
        '''
        raise NotImplementedError