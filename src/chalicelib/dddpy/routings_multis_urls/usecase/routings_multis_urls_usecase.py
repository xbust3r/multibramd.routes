
from chalicelib.dddpy.routings_multis_urls.usecase.routings_multis_urls_cmd_schema import (
    CreateRoutingMultiUrlSchema,
    UpdateRoutingMultiUrlSchema,
)
from chalicelib.dddpy.routings_multis_urls.domain.routings_multis_urls_exception import (
    RoutingsMultisUrlsNotFoundError,
    RoutingMultiUrlNotFoundError,
    RoutingMultiUrlAlreadyExistsError,
)
from chalicelib.dddpy.routings_multis_urls.domain.routings_multis_urls_success import (
    RoutingMultiUrlSuccessMessages,
)

from chalicelib.dddpy.routings_multis_urls.usecase.routings_multis_urls_factory import (
    routing_multi_url_cmd_usecase_factory, routing_multi_url_query_usecase_factory
)
from chalicelib.dddpy.shared.schemas.response_schema import (
    ResponseSuccessSchema,
    ResponseErrorSchema,
)


class RoutingMultiUrlUsecase:
    """
    This class represents the use case for managing routing multi URLs.
    """

    def __init__(self) -> None:
        """
        Initializes the RoutingMultiUrlUsecase.
        """
        self.routing_multi_url_cmd_usecase = routing_multi_url_cmd_usecase_factory()
        self.routing_multi_url_query_usecase = routing_multi_url_query_usecase_factory()

    def create(self, routing_multi: CreateRoutingMultiUrlSchema):
        """
        Creates a new routing multi URL.

        Args:
            routing_multi (CreateRoutingMultiUrlSchema): The routing multi URL data.

        Returns:
            ResponseSuccessSchema or ResponseErrorSchema: The response schema indicating success or error.
        """
        try:
            routing_multi = self.routing_multi_url_cmd_usecase.create(routing_multi)
            return ResponseSuccessSchema(
                message=RoutingMultiUrlSuccessMessages.ROUTING_MULTI_CREATED,
                data=routing_multi.to_dict(),
            )
        except RoutingMultiUrlAlreadyExistsError as e:
            return ResponseErrorSchema(message=str(e))
        except Exception as e:
            return ResponseErrorSchema(message=str(e))

    def find_by_routing_multi_id_and_order(self, routing_multi_id: int, order: int):
        """
        Finds a routing multi URL by routing multi ID and order.

        Args:
            routing_multi_id (int): The ID of the routing multi.
            order (int): The order of the routing multi URL.

        Returns:
            ResponseSuccessSchema or ResponseErrorSchema: The response schema indicating success or error.
        """
        try:
            routing_multi_url = (
                self.routing_multi_url_query_usecase.find_by_routing_multi_id_and_order(
                    routing_multi_id, order
                )
            )
            return ResponseSuccessSchema(
                message=RoutingMultiUrlSuccessMessages.ROUTING_MULTI_URL_FOUND,
                data=routing_multi_url.to_dict(),
            )
        except RoutingMultiUrlNotFoundError as e:
            return ResponseErrorSchema(message=str(e))
        except Exception as e:
            return ResponseErrorSchema(message=str(e))
