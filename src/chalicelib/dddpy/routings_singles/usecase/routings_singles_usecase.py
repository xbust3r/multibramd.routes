from chalicelib.dddpy.routings_singles.domain.routings_singles_exception import (SingleRoutingNotFoundError, SingleRoutingAlreadyExistsError)
from chalicelib.dddpy.routings_singles.usecase.routings_singles_cmd_schema import (CreateSingleRoutingSchema, UpdateSingleRoutingSchema)
from chalicelib.dddpy.routings_singles.domain.routings_singles_success import (SingleRoutingSuccessMessages)
from chalicelib.dddpy.routings_singles.usecase.routings_singles_factory import (single_routing_cmd_usecase_factory, single_routing_query_usecase_factory)
from chalicelib.dddpy.shared.schemas.response_schema import (ResponseSuccessSchema, ResponseErrorSchema)

class RoutingSingleUsecase:
    """
    This class represents the use case for single routings.
    It provides methods for creating and finding single routings.
    """

    def __init__(self) -> None:
        """
        Initializes the RoutingSingleUsecase object.
        """
        self.routing_single_cmd_usecase = single_routing_cmd_usecase_factory()
        self.routing_single_query_usecase = single_routing_query_usecase_factory()
        
    def create(self, routing_single: CreateSingleRoutingSchema):
        """
        Creates a single routing.

        Args:
            routing_single (CreateSingleRoutingSchema): The schema representing the single routing.

        Returns:
            ResponseSuccessSchema: The success response schema with the created single routing data.

        Raises:
            Exception: If an error occurs during the creation process.
        """
        try:
            routing_single = self.routing_single_cmd_usecase.create(routing_single)
            return ResponseSuccessSchema(
                message=SingleRoutingSuccessMessages.CREATE_SUCCESS,
                data=routing_single.to_dict(),
            )
        except Exception as e:
            raise e
        
    def find_by_configuration_id(self, configuration_id: int):
        """
        Finds a single routing by configuration ID.

        Args:
            configuration_id (int): The ID of the configuration.

        Returns:
            ResponseSuccessSchema: The success response schema with the found single routing data.

        Raises:
            Exception: If an error occurs during the finding process.
        """
        try:
            routing_single = self.routing_single_query_usecase.find_by_configuration_id(configuration_id)
            return ResponseSuccessSchema(
                message=SingleRoutingSuccessMessages.FIND_BY_CONFIGURATION_ID_SUCCESS,
                data=routing_single.to_dict(),
            )
        except Exception as e:
            raise e
        
    def find_by_id(self, id: int):
        """
        Finds a single routing by ID.

        Args:
            id (int): The ID of the single routing.

        Returns:
            ResponseSuccessSchema: The success response schema with the found single routing data.

        Raises:
            SingleRoutingNotFoundError: If the single routing is not found.
            Exception: If an error occurs during the finding process.
        """
        try:
            routing_single = self.routing_single_query_usecase.find_by_id(id)
            if routing_single is None:
                raise SingleRoutingNotFoundError()
            return ResponseSuccessSchema(
                message=SingleRoutingSuccessMessages.FIND_BY_ID_SUCCESS,
                data=routing_single.to_dict(),
            )
        except Exception as e:
            raise e
    
    def find_by_routing_id(self, routing_id: int):
        """
        Finds a single routing by routing ID.

        Args:
            routing_id (int): The ID of the routing.

        Returns:
            ResponseSuccessSchema: The success response schema with the found single routing data.

        Raises:
            SingleRoutingNotFoundError: If the single routing is not found.
            Exception: If an error occurs during the finding process.
        """
        try:
            routing_single = self.routing_single_query_usecase.find_by_routing_id(routing_id)
            if routing_single is None:
                raise SingleRoutingNotFoundError()
            return ResponseSuccessSchema(
                message=SingleRoutingSuccessMessages.FIND_BY_ID_SUCCESS,
                data=routing_single.to_dict(),
            )
        except Exception as e:
            raise e