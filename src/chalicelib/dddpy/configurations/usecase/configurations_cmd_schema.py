
from pydantic import BaseModel, Field
from typing import Optional, List

class CreateConfigurationSchema(BaseModel):
    """
    Schema for creating a configuration.
    """
    title: str
    language: str
    insurance: str
    device: str
    media: str
    state: str
    type: int
    brand_id: int
    brand: str
    system: str


class UpdateConfigurationSchema(BaseModel):
    """
    Schema for updating a configuration.
    """
    title: Optional[str]
    language: Optional[str]
    insurance: Optional[str]
    device: Optional[str]
    media: Optional[str]
    state: Optional[str]
    type: Optional[int]
    brand_id: Optional[int]
    brand: Optional[str]
    system: Optional[str]
