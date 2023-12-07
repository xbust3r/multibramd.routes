from pydantic import BaseModel, Json
from typing import Optional, List, Dict, Any, Union
from datetime import datetime

class CreateLogSchema(BaseModel):
    """
    Represents the schema for creating a log entry.

    Attributes:
        response (dict): The response data.
        status (bool): The status of the log entry.
        ip (str): The IP address.
        brand_id (int): The brand ID.
        language (str): The language.
    """
    response: dict
    status: bool
    ip: str
    brand_id: int
    language: str
    

