
from pydantic import BaseModel, Field
from typing import Optional, List


class ListDomainsSchema(BaseModel):
    """
    Schema for listing domains.
    """
    urls: List[str]


class CreateGeneatorSchema(BaseModel):
    """
    Schema for creating a generator.
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
    urls: List[str]
