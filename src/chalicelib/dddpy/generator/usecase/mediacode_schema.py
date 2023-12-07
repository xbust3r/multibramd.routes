
from pydantic import BaseModel, Field
from typing import Optional, List

class MediacodeSchema(BaseModel):
    """
    Represents the schema for a mediacode.

    Attributes:
        zip_code (int): The zip code.
        device (str): The device.
        language (str): The language.
        type_insurance (str): The type of insurance.
        media (str): The media.
        brand (str): The brand.
    """
    zip_code: int
    device: str
    language: str
    type_insurance: str
    media: str
    brand: str
    
class UrlReplaceSchema(BaseModel):
    """
    Represents the schema for URL replacement.

    Attributes:
        url (str): The URL.
        mediacode (str, optional): The mediacode.
        phone (str, optional): The phone number.
        zip_code (str, optional): The zip code.
        city (str, optional): The city.
        state (str, optional): The state.
        system (str): The system.
    """
    url: str
    mediacode: Optional[str]
    phone: Optional[str]
    zip_code: Optional[str]
    city: Optional[str]
    state: Optional[str]
    system: str