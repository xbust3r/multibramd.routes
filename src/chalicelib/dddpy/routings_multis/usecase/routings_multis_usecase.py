from chalicelib.dddpy.routings_multis.usecase.routings_multis_cmd_schema import (
    CreateRoutingMultiSchema,
    UpdateRoutingMultiSchema,
)
from chalicelib.dddpy.routings_multis.domain.routings_multis_exception import (
    RoutingsMultisNotFoundError,
    RoutingMultiNotFoundError,
    RoutingMultiAlreadyExistsError,
)
from chalicelib.dddpy.routings_multis.domain.routings_multis_success import (
    RoutingMultiSuccessMessages,
)

from chalicelib.dddpy.routings_multis.usecase.routings_multis_factory import (
    routing_multi_cmd_usecase_factory,
    routing_multi_query_usecase_factory,
)
from chalicelib.dddpy.shared.schemas.response_schema import (
    ResponseSuccessSchema,
    ResponseErrorSchema,
)


class RoutingMultiUsecase:
    """
    This class represents the use case for managing routing multi entities.
    """

    def __init__(self) -> None:
        """
        Initializes the RoutingMultiUsecase object.
        """
        self.routing_multi_cmd_usecase = routing_multi_cmd_usecase_factory()
        self.routing_multi_query_usecase = routing_multi_query_usecase_factory()

    def create(self, routing_multi: CreateRoutingMultiSchema):
        """
        Creates a new routing multi entity.

        Args:
            routing_multi (CreateRoutingMultiSchema): The routing multi data.

        Returns:
            ResponseSuccessSchema or ResponseErrorSchema: The response schema indicating success or error.
        """
        try:
            routing_multi = self.routing_multi_cmd_usecase.create(routing_multi)
            return ResponseSuccessSchema(
                message=RoutingMultiSuccessMessages.ROUTING_MULTI_CREATED,
                data=routing_multi.to_dict(),
            )
        except RoutingMultiAlreadyExistsError as e:
            return ResponseErrorSchema(message=str(e))
        except Exception as e:
            return ResponseErrorSchema(message=str(e))

    def find_by_id(self, id: int):
        """
        Finds a routing multi entity by its ID.

        Args:
            id (int): The ID of the routing multi.

        Returns:
            ResponseSuccessSchema or ResponseErrorSchema: The response schema indicating success or error.
        """
        try:
            routing_multi = self.routing_multi_query_usecase.find_by_id(id)
            return ResponseSuccessSchema(
                message=RoutingMultiSuccessMessages.ROUTING_MULTI_FOUND,
                data=routing_multi.to_dict(),
            )
        except RoutingMultiNotFoundError as e:
            return ResponseErrorSchema(message=str(e))
        except Exception as e:
            return ResponseErrorSchema(message=str(e))

    def find_by_configuration_id(self, configuration_id: int):
        """
        Finds a routing multi entity by its configuration ID.

        Args:
            configuration_id (int): The configuration ID of the routing multi.

        Returns:
            ResponseSuccessSchema or ResponseErrorSchema: The response schema indicating success or error.
        """
        try:
            routing_multi = self.routing_multi_query_usecase.find_by_configuration_id(configuration_id)
            return ResponseSuccessSchema(
                message=RoutingMultiSuccessMessages.ROUTING_MULTI_FOUND,
                data=routing_multi.to_dict(),
            )
        except RoutingMultiNotFoundError as e:
            return ResponseErrorSchema(message=str(e))
        except Exception as e:
            return ResponseErrorSchema(message=str(e))

    def update_current_by_id(self, id: int, current: int):
        """
        Updates the current value of a routing multi entity by its ID.

        Args:
            id (int): The ID of the routing multi.
            current (int): The new value of the current field.

        Returns:
            ResponseSuccessSchema or ResponseErrorSchema: The response schema indicating success or error.
        """
        try:
            routing_multi = self.routing_multi_cmd_usecase.update_current_by_id(id, current)
            return ResponseSuccessSchema(
                message=RoutingMultiSuccessMessages.ROUTING_MULTI_UPDATED,
                data=routing_multi.to_dict(),
            )
        except RoutingMultiNotFoundError as e:
            return ResponseErrorSchema(message=str(e))
        except Exception as e:
            return ResponseErrorSchema(message=str(e))