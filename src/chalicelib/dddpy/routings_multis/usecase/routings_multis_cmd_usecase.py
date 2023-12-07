from chalicelib.dddpy.routings_multis.domain.routings_multis_repository import (
    RoutingMultiRepository,
)
from chalicelib.dddpy.routings_multis.usecase.routings_multis_cmd_schema import (
    CreateRoutingMultiSchema,
    UpdateRoutingMultiSchema,
)


class RoutingMultiCmdUsecase:
    """
    This class represents the use case for handling routing multi commands.

    Args:
        repository (RoutingMultiRepository): The repository for routing multi entities.

    """

    def __init__(self, repository: RoutingMultiRepository):
        self.repository = repository

    def create(self, data: CreateRoutingMultiSchema):
        """
        Creates a new routing multi entity.

        Args:
            data (CreateRoutingMultiSchema): The data for creating the routing multi entity.

        Returns:
            The created routing multi entity.

        """
        return self.repository.create(data)

    def update_current_by_id(self, id: int, current: int):
        """
        Updates the current value of a routing multi entity by its ID.

        Args:
            id (int): The ID of the routing multi entity.
            current (int): The new value for the current field.

        Returns:
            The updated routing multi entity.

        """
        return self.repository.update_current_by_id(id, current)
