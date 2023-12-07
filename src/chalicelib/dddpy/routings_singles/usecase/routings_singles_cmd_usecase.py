from chalicelib.dddpy.routings_singles.domain.routings_singles_repository import RoutingSingleRepository
from chalicelib.dddpy.routings_singles.usecase.routings_singles_cmd_schema import (
    CreateSingleRoutingSchema,
    UpdateSingleRoutingSchema,
)

class RoutingSingleCmdUsecase:
    """
    This class represents the use case for handling single routing commands.
    It provides methods for creating single routings.
    """

    def __init__(self, repository: RoutingSingleRepository):
        """
        Initializes a new instance of the RoutingSingleCmdUsecase class.

        Args:
            repository (RoutingSingleRepository): The repository for single routings.
        """
        self.repository=repository
        
    def create(self, data: CreateSingleRoutingSchema):
        """
        Creates a new single routing.

        Args:
            data (CreateSingleRoutingSchema): The data for creating the single routing.

        Returns:
            [type]: The created single routing.
        """
        return self.repository.create(data)
    
    