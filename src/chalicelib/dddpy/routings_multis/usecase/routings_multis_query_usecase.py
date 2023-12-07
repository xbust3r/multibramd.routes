from chalicelib.dddpy.routings_multis.domain.routings_multis_repository import RoutingMultiRepository


class RoutingMultiQueryUsecase:
    """
    This class represents the use case for querying routing multis.
    """

    def __init__(self, routing_multi_repository: RoutingMultiRepository) -> None:
        """
        Initializes a new instance of the RoutingMultiQueryUsecase class.

        Parameters:
        - routing_multi_repository (RoutingMultiRepository): The repository for routing multis.
        """
        self.routing_multi_repository = routing_multi_repository

    def find_by_id(self, id: int):
        """
        Finds a routing multi by its ID.

        Parameters:
        - id (int): The ID of the routing multi.

        Returns:
        - The routing multi with the specified ID.
        """
        return self.routing_multi_repository.find_by_id(id)

    def find_by_configuration_id(self, configuration_id: int):
        """
        Finds routing multis by their configuration ID.

        Parameters:
        - configuration_id (int): The ID of the configuration.

        Returns:
        - A list of routing multis with the specified configuration ID.
        """
        return self.routing_multi_repository.find_by_configuration_id(configuration_id)