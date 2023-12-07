"""
This module provides factory functions for creating instances of the routing multi use cases.

The factory functions defined in this module are:
- routing_multi_cmd_usecase_factory: Returns an instance of the RoutingMultiCmdUsecase class.
- routing_multi_query_usecase_factory: Returns an instance of the RoutingMultiQueryUsecase class.
"""

from chalicelib.dddpy.routings_multis.infrastructure.routings_multis_cmd_repository import RoutingMultiCmdRepositoryImpl
from chalicelib.dddpy.routings_multis.usecase.routings_multis_cmd_usecase import RoutingMultiCmdUsecase

from chalicelib.dddpy.routings_multis.infrastructure.routings_multis_query_repository import RoutingMultiQueryRepositoryImpl
from chalicelib.dddpy.routings_multis.usecase.routings_multis_query_usecase import RoutingMultiQueryUsecase


def routing_multi_cmd_usecase_factory():
    """
    Factory function for creating an instance of the RoutingMultiCmdUsecase class.

    Returns:
        RoutingMultiCmdUsecase: An instance of the RoutingMultiCmdUsecase class.
    """
    return RoutingMultiCmdUsecase(RoutingMultiCmdRepositoryImpl())


def routing_multi_query_usecase_factory():
    """
    Factory function for creating an instance of the RoutingMultiQueryUsecase class.

    Returns:
        RoutingMultiQueryUsecase: An instance of the RoutingMultiQueryUsecase class.
    """
    return RoutingMultiQueryUsecase(RoutingMultiQueryRepositoryImpl())