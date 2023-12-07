
from datetime import datetime
from typing import Optional

from chalicelib.dddpy.configurations.infrastructure.configurations import (
    DBConfiguration,
)


class Configuration:
    """
    Represents a configuration entity.

    Attributes:
        id (int): The ID of the configuration.
        title (str): The title of the configuration.
        language (str): The language of the configuration.
        insurance (str): The insurance of the configuration.
        device (str): The device of the configuration.
        media (str): The media of the configuration.
        state (str): The state of the configuration.
        type (int): The type of the configuration.
        brand_id (int): The brand ID of the configuration.
        brand (str): The brand of the configuration.
        system (str): The system of the configuration.
        created_at (datetime): The creation timestamp of the configuration.
        updated_at (datetime): The last update timestamp of the configuration.
    """

    def __init__(
        self,
        id: int,
        title: str,
        language: str,
        insurance: str,
        device: str,
        media: str,
        state: str,
        type: int,
        brand_id: int,
        brand: str,
        system: str,
        created_at: datetime,
        updated_at: datetime,
    ):
        self.id = id
        self.title = title
        self.language = language
        self.insurance = insurance
        self.device = device
        self.media = media
        self.state = state
        self.type = type
        self.brand_id = brand_id
        self.brand = brand
        self.system = system
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def from_db(cls, db_configuration: DBConfiguration) -> "Configuration":
        """
        Create a Configuration instance from a DBConfiguration instance.

        Args:
            db_configuration (DBConfiguration): The DBConfiguration instance.

        Returns:
            Configuration: The created Configuration instance.
        """
        return cls(
            id=db_configuration.id,
            title=db_configuration.title,
            language=db_configuration.language,
            insurance=db_configuration.insurance,
            device=db_configuration.device,
            media=db_configuration.media,
            state=db_configuration.state,
            type=db_configuration.type,
            brand_id=db_configuration.brand_id,
            brand=db_configuration.brand,
            system=db_configuration.system,
            created_at=db_configuration.created_at,
            updated_at=db_configuration.updated_at,
        )

    @classmethod
    def to_db(cls, configuration: "Configuration") -> DBConfiguration:
        """
        Convert a Configuration instance to a DBConfiguration instance.

        Args:
            configuration (Configuration): The Configuration instance.

        Returns:
            DBConfiguration: The converted DBConfiguration instance.
        """
        return DBConfiguration(
            id=configuration.id,
            title=configuration.title,
            language=configuration.language,
            insurance=configuration.insurance,
            device=configuration.device,
            media=configuration.media,
            state=configuration.state,
            type=configuration.type,
            brand_id=configuration.brand_id,
            brand=configuration.brand,
            system=configuration.system,
            created_at=configuration.created_at,
            updated_at=configuration.updated_at,
        )

    def to_dict(self) -> dict:
        """
        Convert the Configuration instance to a dictionary.

        Returns:
            dict: The dictionary representation of the Configuration instance.
        """
        return {
            "id": self.id,
            "title": self.title,
            "language": self.language,
            "insurance": self.insurance,
            "device": self.device,
            "media": self.media,
            "state": self.state,
            "type": self.type,
            "brand_id": self.brand_id,
            "brand": self.brand,
            "system": self.system,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
