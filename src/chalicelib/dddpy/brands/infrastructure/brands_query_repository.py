from chalicelib.dddpy.shared.mysql.base import SessionLocal
from chalicelib.dddpy.brands.domain.brands_repository import BrandRepository
from chalicelib.dddpy.brands.infrastructure.brands import DBBrands
from chalicelib.dddpy.brands.domain.brands import Brand
from chalicelib.dddpy.shared.mysql.session_manager import session_scope

class BrandQueryRepositoryImpl(BrandRepository):
    """
    Implementation of the BrandRepository interface for querying brands from the database.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the BrandQueryRepositoryImpl class.
        """
        self.session = SessionLocal()

    def find_by_code(self, code: str):
        """
        Finds a brand by its code.

        Args:
            code (str): The code of the brand to find.

        Returns:
            Brand: The brand with the specified code, or None if not found.
        """
        with session_scope() as session:
            brand = session.query(DBBrands).filter(DBBrands.brand_code == code).first()
            if brand is None:
                return None
            return Brand.from_db(brand)
            