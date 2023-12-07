
from pydantic import BaseModel, Field
from typing import Optional, List

class GetUrlSchema(BaseModel):
    """
    Represents the schema for generating a URL.

    Args:
        language (str): The language of the URL.
        insurance (str): The insurance of the URL.
        device (str): The device of the URL.
        media (str): The media of the URL.
        brand (str): The brand of the URL.
        zip_code (int): The zip code of the URL.
        ip (Optional[str], optional): The IP address of the URL. Defaults to None.
    """
    language: str
    insurance: str
    device: str
    media: str
    brand: str
    zip_code: int
    ip: Optional[str] = None
