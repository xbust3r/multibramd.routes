from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class CreateSingleRoutingSchema(BaseModel):
    """
    Schema for creating a single routing.

    Attributes:
        url (str): The URL of the routing.
        domain (str): The domain of the routing.
        variables (dict): The variables associated with the routing.
        configuration_id (int): The ID of the configuration.
        brand_id (Optional[int]): The ID of the brand (optional).
    """
    url: str = Field(..., example="https://www.google.com")
    domain: str = Field(..., example="google.com")
    variables: dict = Field(..., example={"key": "value"})
    configuration_id: int = Field(..., example=1)
    brand_id: Optional[int] = Field(None, example=1)


class UpdateSingleRoutingSchema(BaseModel):
    """
    Schema for updating a single routing.

    Attributes:
        url (str): The URL of the routing.
        domain (str): The domain of the routing.
        variables (dict): The variables associated with the routing.
        configuration_id (int): The ID of the configuration.
        brand_id (Optional[int]): The ID of the brand (optional).
    """
    url: str = Field(..., example="https://www.google.com")
    domain: str = Field(..., example="google.com")
    variables: dict = Field(..., example={"key": "value"})
    configuration_id: int = Field(..., example=1)
    brand_id: Optional[int] = Field(None, example=1)
