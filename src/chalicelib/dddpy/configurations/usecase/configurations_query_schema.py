
from pydantic import BaseModel, Field
from typing import Optional, List

class CheckDuplicatedConfigurationSchema(BaseModel):
    '''
    Schema for checking duplicated configurations.
    '''
    language: str
    insurance: str
    device: str
    media: str
    state: str
    type: int
    brand_id: int


class FindConfigurationSchema(BaseModel):
    '''
    Schema for finding configurations.
    '''
    language: str
    insurance: str
    device: str
    media: str
    state: str
    brand_id: int