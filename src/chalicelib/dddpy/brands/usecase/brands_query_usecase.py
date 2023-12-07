

from chalicelib.dddpy.brands.domain.brands_repository import BrandRepository

class BrandQueryUsecase:
    """
    This class represents the use case for querying brands by code.
    """

    def __init__(self, brand_repository: BrandRepository) -> None:
        """
        Initializes a new instance of the BrandQueryUsecase class.

        Args:
            brand_repository (BrandRepository): The repository for accessing brand data.
        """
        self.brand_repository = brand_repository

    def find_by_code(self, code: str):
        """
        Finds a brand by its code.

        Args:
            code (str): The code of the brand to find.

        Returns:
            The brand with the specified code, or None if not found.
        """
        return self.brand_repository.find_by_code(code)