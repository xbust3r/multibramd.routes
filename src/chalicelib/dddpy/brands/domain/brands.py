from datetime import datetime
from typing import Optional

from chalicelib.dddpy.brands.infrastructure.brands import DBBrands


class Brand:
    """
    Represents a brand entity.

    Args:
        brand (str): The brand name.
        brand_code (str): The brand code.
        description (str): The brand description.
        id (Optional[int]): The brand ID. Defaults to None.
        brand_id (Optional[int]): The brand ID. Defaults to None.
        created_at (Optional[datetime]): The creation timestamp. Defaults to None.
        updated_at (Optional[datetime]): The update timestamp. Defaults to None.
    """

    def __init__(
        self,
        brand: str,
        brand_code: str,
        description: str,
        id: Optional[int] = None,
        brand_id: Optional[int] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> None:
        self.id = id
        self.brand = brand
        self.brand_code = brand_code
        self.description = description
        self.brand_id = brand_id
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def from_db(cls, db_brand: DBBrands) -> "Brand":
        """
        Create a Brand instance from a DBBrands instance.

        Args:
            db_brand (DBBrands): The DBBrands instance.

        Returns:
            Brand: The created Brand instance.
        """
        return cls(
            id=db_brand.id,
            brand=db_brand.brand,
            brand_code=db_brand.brand_code,
            description=db_brand.description,
            brand_id=db_brand.brand_id,
            created_at=db_brand.created_at,
            updated_at=db_brand.updated_at,
        )

    @classmethod
    def to_db(cls, brand: "Brand") -> DBBrands:
        """
        Convert a Brand instance to a DBBrands instance.

        Args:
            brand (Brand): The Brand instance.

        Returns:
            DBBrands: The converted DBBrands instance.
        """
        return DBBrands(
            id=brand.id,
            brand=brand.brand,
            description=brand.description,
            brand_id=brand.brand_id,
            brand_code=brand.brand_code,
            created_at=brand.created_at,
            updated_at=brand.updated_at,
        )

    def to_dict(self) -> dict:
        """
        Convert the Brand instance to a dictionary.

        Returns:
            dict: The dictionary representation of the Brand instance.
        """
        return {
            "id": self.id,
            "brand": self.brand,
            "brand_code": self.brand_code,
            "description": self.description,
            "brand_id": self.brand_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
