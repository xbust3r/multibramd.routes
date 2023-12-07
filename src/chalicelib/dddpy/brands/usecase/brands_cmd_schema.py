'''
This file contains Pydantic models for handling brand data.

The CreateBrandSchema model represents the data required to create a new brand.
The UpdateBrandSchema model represents the data that can be updated for an existing brand.
The ReturnBrandSchema model represents the data that is returned when querying for a brand.
'''

from pydantic import BaseModel, Field, validator
from typing import Optional, List, Dict, Any, Union
from datetime import datetime

class CreateBrandSchema(BaseModel):
    '''
    Represents the data required to create a new brand.

    Attributes:
        brand (str): The brand name.
        description (str): The brand description.
        brand_code (str): The brand code.
        brand_id (Optional[int]): The brand ID (optional).
    '''
    brand: str
    description: str
    brand_code: str
    brand_id: Optional[int] = None

class UpdateBrandSchema(BaseModel):
    '''
    Represents the data that can be updated for an existing brand.

    Attributes:
        brand (Optional[str]): The updated brand name (optional).
        brand_code (Optional[str]): The updated brand code (optional).
        description (Optional[str]): The updated brand description (optional).
        brand_id (Optional[int]): The brand ID (optional).
    '''
    brand: Optional[str] = None
    brand_code: Optional[str] = None
    description: Optional[str] = None
    brand_id: Optional[int] = None

class ReturnBrandSchema(BaseModel):
    '''
    Represents the data that is returned when querying for a brand.

    Attributes:
        brand (str): The brand name.
        description (str): The brand description.
        brand_id (Optional[int]): The brand ID (optional).
        created_at (Optional[datetime]): The creation timestamp (optional).
        updated_at (Optional[datetime]): The update timestamp (optional).
    '''
    brand: str
    description: str
    brand_id: Optional[int]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
