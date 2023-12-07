from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class CreateRoutingMultiUrlSchema(BaseModel):
    """
    Schema for creating a routing multi URL.

    Attributes:
        url (str): The URL.
        domain (str): The domain.
        routing_multi_id (int): The ID of the routing multi.
        order (int): The order of the URL.
    """
    url: str = Field(..., example="https://www.google.com")
    domain: str = Field(..., example="google.com")
    routing_multi_id: int = Field(..., example=1)
    order: int = Field(..., example=1)

class UpdateRoutingMultiUrlSchema(BaseModel):
    """
    Schema for updating a routing multi URL.

    Attributes:
        url (str): The URL.
        domain (str): The domain.
        routing_multi_id (int): The ID of the routing multi.
        order (int): The order of the URL.
    """
    url: str = Field(..., example="https://www.google.com")
    domain: str = Field(..., example="google.com")
    routing_multi_id: int = Field(..., example=1)
    order: int = Field(..., example=1)