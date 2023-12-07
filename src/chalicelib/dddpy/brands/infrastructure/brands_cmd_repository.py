from chalicelib.dddpy.brands.domain.brands import Brand
from chalicelib.dddpy.brands.domain.brands_repository import BrandRepository
from chalicelib.dddpy.brands.usecase.brands_cmd_schema import CreateBrandSchema, UpdateBrandSchema
from chalicelib.dddpy.brands.infrastructure.brands import DBBrands

from chalicelib.dddpy.shared.mysql.base import SessionLocal
from chalicelib.dddpy.shared.timezone import Timezone

from chalicelib.dddpy.shared.mysql.session_manager import session_scope


class BrandCmdRepositoryImpl(BrandRepository):
    """
    Implementation of the BrandRepository interface for the command side of the application.

    This repository is responsible for persisting and retrieving Brand entities in the database.

    Attributes:
        session (SessionLocal): The database session used for interacting with the database.

    """

    def __init__(self) -> None:
        self.session = SessionLocal()
        
    def create(self, data: CreateBrandSchema) -> Brand:
        """
        Create a new Brand entity in the database.

        Args:
            data (CreateBrandSchema): The data required to create a new Brand.

        Returns:
            Brand: The created Brand entity.

        """
        with session_scope() as session:
            today=Timezone.get_datetime()
            brand = Brand(
                brand=data.brand,
                brand_code=data.brand_code,
                description=data.description,
                brand_id=data.brand_id,
                created_at=today,
                updated_at=today,
            )
            new_brand=Brand.to_db(brand)
            session.add(new_brand)
            session.commit()
            session.refresh(new_brand)
            return Brand.from_db(new_brand)