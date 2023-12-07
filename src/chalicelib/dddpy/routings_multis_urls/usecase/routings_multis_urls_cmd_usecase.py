from chalicelib.dddpy.routings_multis_urls.domain.routings_multis_urls_repository import (
    RoutingMultiUrlRepository,
)
from chalicelib.dddpy.routings_multis_urls.usecase.routings_multis_urls_cmd_schema import (
    CreateRoutingMultiUrlSchema,
    UpdateRoutingMultiUrlSchema,
)


class RoutingMultiUrlCmdUsecase:
    """
    This class represents the use case for creating and managing routing multi URLs.

    Args:
        repository (RoutingMultiUrlRepository): The repository for accessing routing multi URLs.

    """

    def __init__(self, repository: RoutingMultiUrlRepository):
        self.repository = repository

    def create(self, data: CreateRoutingMultiUrlSchema):
        """
        Create a new routing multi URL.

        Args:
            data (CreateRoutingMultiUrlSchema): The data for creating the routing multi URL.

        Returns:
            RoutingMultiUrl: The created routing multi URL.

        """
        return self.repository.create(data)
