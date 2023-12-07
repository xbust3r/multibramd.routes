
from chalicelib.dddpy.brands.usecase.brands_cmd_schema import CreateBrandSchema, UpdateBrandSchema
from chalicelib.dddpy.brands.domain.brands_repository import BrandRepository

class BrandCmdUsecase:
    """
    This class represents the use case for brand commands.
    It provides methods for creating, updating, and deleting brands.
    """

    def __init__(self, repository: BrandRepository) -> None:
        """
        Initializes a new instance of the BrandCmdUsecase class.

        Args:
            repository (BrandRepository): The repository for brand data.
        """
        self.repository = repository
    
    def create(self, data: CreateBrandSchema):
        """
        Creates a new brand.

        Args:
            data (CreateBrandSchema): The data for creating the brand.

        Returns:
            The created brand.
        """
        return self.repository.create(data)
    
    def update(self, id: int, data: UpdateBrandSchema):
        """
        Updates an existing brand.

        Args:
            id (int): The ID of the brand to update.
            data (UpdateBrandSchema): The updated data for the brand.

        Returns:
            The updated brand.
        """
        return self.repository.update(id, data)
    
    def delete(self, id: int):
        """
        Deletes an existing brand.

        Args:
            id (int): The ID of the brand to delete.

        Returns:
            None
        """
        return self.repository.delete(id)