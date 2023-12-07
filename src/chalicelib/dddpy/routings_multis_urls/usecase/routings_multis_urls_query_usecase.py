from chalicelib.dddpy.routings_multis_urls.domain.routings_multis_urls_repository import (
    RoutingMultiUrlRepository,
)


class RoutingMultiUrlQueryUsecase:
    """
    This class represents the use case for querying routing multi URLs.
    """

    def __init__(self, routing_multi_url_repository: RoutingMultiUrlRepository) -> None:
        """
        Initializes a new instance of the RoutingMultiUrlQueryUsecase class.

        Args:
            routing_multi_url_repository (RoutingMultiUrlRepository): The repository for routing multi URLs.
        """
        self.routing_multi_url_repository = routing_multi_url_repository

    def find_by_id(self, id: int):
        """
        Finds a routing multi URL by its ID.

        Args:
            id (int): The ID of the routing multi URL.

        Returns:
            The routing multi URL with the specified ID.
        """
        return self.routing_multi_url_repository.find_by_id(id)

    def find_by_routing_multi_id(self, routing_multi_id: int):
        """
        Finds routing multi URLs by their routing multi ID.

        Args:
            routing_multi_id (int): The ID of the routing multi.

        Returns:
            A list of routing multi URLs with the specified routing multi ID.
        """
        return self.routing_multi_url_repository.find_by_routing_multi_id(
            routing_multi_id
        )

    def find_by_routing_multi_id_and_order(self, routing_multi_id: int, order: int):
        """
        Finds a routing multi URL by its routing multi ID and order.

        Args:
            routing_multi_id (int): The ID of the routing multi.
            order (int): The order of the routing multi URL.

        Returns:
            The routing multi URL with the specified routing multi ID and order.
        """
        return self.routing_multi_url_repository.find_by_routing_multi_id_and_order(
            routing_multi_id, order
        )
