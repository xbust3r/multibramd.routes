"""
This module provides factory functions for creating instances of the routing multi URL use cases.

The factory functions defined in this module are:
- routing_multi_url_cmd_usecase_factory: Returns an instance of the RoutingMultiUrlCmdUsecase class.
- routing_multi_url_query_usecase_factory: Returns an instance of the RoutingMultiUrlQueryUsecase class.
"""

from chalicelib.dddpy.routings_multis_urls.infrastructure.routings_multis_urls_cmd_repository import RoutingMultiUrlCmdRepositoryImpl
from chalicelib.dddpy.routings_multis_urls.usecase.routings_multis_urls_cmd_usecase import RoutingMultiUrlCmdUsecase
from chalicelib.dddpy.routings_multis_urls.usecase.routings_multis_urls_query_usecase import RoutingMultiUrlQueryUsecase
from chalicelib.dddpy.routings_multis_urls.infrastructure.routings_multis_urls_query_repository import RoutingMultiUrlQueryRepositoryImpl


def routing_multi_url_cmd_usecase_factory():
    """
    Factory function for creating an instance of the RoutingMultiUrlCmdUsecase class.

    Returns:
        RoutingMultiUrlCmdUsecase: An instance of the RoutingMultiUrlCmdUsecase class.
    """
    return RoutingMultiUrlCmdUsecase(RoutingMultiUrlCmdRepositoryImpl())


def routing_multi_url_query_usecase_factory():
    """
    Factory function for creating an instance of the RoutingMultiUrlQueryUsecase class.

    Returns:
        RoutingMultiUrlQueryUsecase: An instance of the RoutingMultiUrlQueryUsecase class.
    """
    return RoutingMultiUrlQueryUsecase(RoutingMultiUrlQueryRepositoryImpl())