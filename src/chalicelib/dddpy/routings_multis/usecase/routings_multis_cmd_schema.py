from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class CreateRoutingMultiSchema(BaseModel):
    """
    Schema for creating a routing multi.
    """

    configuration_id: int = Field(..., example=1)
    brand_id: Optional[int] = Field(None, example=1)
    total: int = Field(..., example=1)
    variables: Optional[dict] = Field(None, example={"key": "value"})

class UpdateRoutingMultiSchema(BaseModel):
    """
    Schema for updating a routing multi.
    """

    configuration_id: int = Field(..., example=1)
    brand_id: Optional[int] = Field(None, example=1)
    total: int = Field(..., example=1)
    variables: Optional[dict] = Field(None, example={"key": "value"})