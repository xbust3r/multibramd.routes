from chalicelib.dddpy.routings_singles.usecase.routings_singles_cmd_schema import (
    CreateSingleRoutingSchema,
    UpdateSingleRoutingSchema,
)

class RoutingSingleRepository:
    """
    This class represents a repository for managing single routings.
    """

    def all(self):
        """
        Retrieves all single routings.
        """
        raise NotImplementedError
    
    def find_by_id(self, id: int):
        """
        Finds a single routing by its ID.

        Parameters:
        - id (int): The ID of the single routing.

        Returns:
        - The single routing with the specified ID.
        """
        raise NotImplementedError
    
    def find_by_url(self, url: str):
        """
        Finds a single routing by its URL.

        Parameters:
        - url (str): The URL of the single routing.

        Returns:
        - The single routing with the specified URL.
        """
        raise NotImplementedError
    
    def find_by_domain(self, domain: str):
        """
        Finds a single routing by its domain.

        Parameters:
        - domain (str): The domain of the single routing.

        Returns:
        - The single routing with the specified domain.
        """
        raise NotImplementedError
    
    def find_by_configuration_id(self, configuration_id: int):
        """
        Finds a single routing by its configuration ID.

        Parameters:
        - configuration_id (int): The configuration ID of the single routing.

        Returns:
        - The single routing with the specified configuration ID.
        """
        raise NotImplementedError
    
    def find_by_brand_id(self, brand_id: int):
        """
        Finds a single routing by its brand ID.

        Parameters:
        - brand_id (int): The brand ID of the single routing.

        Returns:
        - The single routing with the specified brand ID.
        """
        raise NotImplementedError
    
    def create(self, single_routing: CreateSingleRoutingSchema):
        """
        Creates a new single routing.

        Parameters:
        - single_routing (CreateSingleRoutingSchema): The schema representing the single routing to be created.
        """
        raise NotImplementedError
    
    def update(self, single_routing: UpdateSingleRoutingSchema):
        """
        Updates an existing single routing.

        Parameters:
        - single_routing (UpdateSingleRoutingSchema): The schema representing the updated single routing.
        """
        raise NotImplementedError
    
    def delete(self, id: int):
        """
        Deletes a single routing by its ID.

        Parameters:
        - id (int): The ID of the single routing to be deleted.
        """
        raise NotImplementedError