
from chalicelib.dddpy.brands.domain.brands_exception import (
    BrandsNotFoundError,
    BrandNotCreatedError,
    BrandAlreadyExistsError,
    BrandNotFoundError,
)
from chalicelib.dddpy.brands.usecase.brands_cmd_schema import (
    CreateBrandSchema,
    UpdateBrandSchema,
    ReturnBrandSchema,
)

from chalicelib.dddpy.brands.domain.brands_success import BrandSucessMessages

from chalicelib.dddpy.brands.usecase.brands_factory import brand_cmd_usecase_factory, brand_query_usecase_factory

from chalicelib.dddpy.shared.schemas.response_schema import (
    ResponseSuccessSchema,
    ResponseErrorSchema,
)

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class BrandUsecase:
    """
    This class represents the use case for managing brands.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the BrandUsecase class.
        """
        self.brand_cmd_usecase = brand_cmd_usecase_factory()
        self.brand_query_usecase = brand_query_usecase_factory()

    def create(self, data: CreateBrandSchema):
        """
        Creates a new brand.

        Args:
            data (CreateBrandSchema): The data for creating the brand.

        Returns:
            ResponseSuccessSchema: The success response containing the created brand data.

        Raises:
            Exception: If an error occurs during the creation process.
        """
        try:
            logger.debug(f"starting BrandUsecase.create: {data}")
            brand = self.brand_cmd_usecase.create(data)

            success = ResponseSuccessSchema(
                message=BrandSucessMessages.BRAND_CREATED,
                data=brand.to_dict(),
            )

            logger.debug(success)
            return success
        except Exception as e:
           raise e
    
    def find_by_code(self, code:str):
        """
        Finds a brand by its code.

        Args:
            code (str): The code of the brand to find.

        Returns:
            ResponseSuccessSchema: The success response containing the found brand data.

        Raises:
            Exception: If an error occurs during the search process.
        """
        try:
            brand = self.brand_query_usecase.find_by_code(code)
            if not brand:
                raise BrandNotFoundError()
            success = ResponseSuccessSchema(
                message=BrandSucessMessages.BRAND_FOUND,
                data=brand.to_dict(),
            )
            return success
        except Exception as e:
            raise e
