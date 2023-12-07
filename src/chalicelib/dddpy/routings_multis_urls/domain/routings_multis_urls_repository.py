from chalicelib.dddpy.routings_multis.usecase.routings_multis_cmd_schema import (CreateRoutingMultiSchema, UpdateRoutingMultiSchema)

class RoutingMultiUrlRepository:
    """
    Repository class for managing routing multi URLs.
    """

    def all(self):
        """
        Retrieve all routing multi URLs.
        """
        raise NotImplementedError
    
    def find_by_id(self, id: int):
        """
        Find a routing multi URL by its ID.

        Args:
            id (int): The ID of the routing multi URL.

        Returns:
            None
        """
        raise NotImplementedError
    
    def create(self, routing_multi: CreateRoutingMultiSchema):
        """
        Create a new routing multi URL.

        Args:
            routing_multi (CreateRoutingMultiSchema): The routing multi URL to create.

        Returns:
            None
        """
        raise NotImplementedError
    
    def update(self, routing_multi: UpdateRoutingMultiSchema):
        """
        Update an existing routing multi URL.

        Args:
            routing_multi (UpdateRoutingMultiSchema): The updated routing multi URL.

        Returns:
            None
        """
        raise NotImplementedError
    
    def delete(self, id: int):
        """
        Delete a routing multi URL by its ID.

        Args:
            id (int): The ID of the routing multi URL to delete.

        Returns:
            None
        """
        raise NotImplementedError
    
    def find_by_routing_multi_id(self, routing_multi_id: int):
        """
        Find routing multi URLs by routing multi ID.

        Args:
            routing_multi_id (int): The ID of the routing multi.

        Returns:
            None
        """
        raise NotImplementedError
    
    def find_by_routing_multi_id_and_order(self, routing_multi_id: int, order: int):
        """
        Find a routing multi URL by routing multi ID and order.

        Args:
            routing_multi_id (int): The ID of the routing multi.
            order (int): The order of the routing multi URL.

        Returns:
            None
        """
        raise NotImplementedError
    