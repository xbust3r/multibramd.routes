from chalicelib.dddpy.routings_multis.usecase.routings_multis_cmd_schema import (CreateRoutingMultiSchema, UpdateRoutingMultiSchema)

class RoutingMultiRepository:
    """
    This class represents a repository for managing routing multi entities.
    """

    def all(self):
        """
        Retrieves all routing multi entities.

        Returns:
            List: A list of all routing multi entities.
        """
        raise NotImplementedError
    
    def find_by_id(self, id: int):
        """
        Retrieves a routing multi entity by its ID.

        Args:
            id (int): The ID of the routing multi entity.

        Returns:
            Any: The routing multi entity with the specified ID.
        """
        raise NotImplementedError
    
    def create(self, routing_multi: CreateRoutingMultiSchema):
        """
        Creates a new routing multi entity.

        Args:
            routing_multi (CreateRoutingMultiSchema): The routing multi entity to create.

        Returns:
            Any: The created routing multi entity.
        """
        raise NotImplementedError
    
    def update(self, routing_multi: UpdateRoutingMultiSchema):
        """
        Updates an existing routing multi entity.

        Args:
            routing_multi (UpdateRoutingMultiSchema): The routing multi entity to update.

        Returns:
            Any: The updated routing multi entity.
        """
        raise NotImplementedError
    
    def delete(self, id: int):
        """
        Deletes a routing multi entity by its ID.

        Args:
            id (int): The ID of the routing multi entity to delete.
        """
        raise NotImplementedError
    
    def find_by_configuration_id(self, configuration_id: int):
        """
        Retrieves routing multi entities by their configuration ID.

        Args:
            configuration_id (int): The configuration ID.

        Returns:
            List: A list of routing multi entities with the specified configuration ID.
        """
        raise NotImplementedError
    
    def update_current_by_id(self, id: int, current: int):
        """
        Updates the current value of a routing multi entity by its ID.

        Args:
            id (int): The ID of the routing multi entity.
            current (int): The new current value.

        Returns:
            Any: The updated routing multi entity.
        """
        raise NotImplementedError
    
    