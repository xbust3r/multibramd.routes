from chalicelib.dddpy.routings_singles.infrastructure.routings_singles_cmd_repository import SIngleRoutingCmdRepositoryImpl
from chalicelib.dddpy.routings_singles.usecase.routings_singles_cmd_usecase import RoutingSingleCmdUsecase
from chalicelib.dddpy.routings_singles.infrastructure.routings_singles_query_repository import RoutingSingleRepositoryImpl
from chalicelib.dddpy.routings_singles.usecase.routings_singles_query_usecase import RoutingSingleQueryUsecase

def single_routing_cmd_usecase_factory():
    """
    Factory function that creates an instance of RoutingSingleCmdUsecase.

    Returns:
        RoutingSingleCmdUsecase: An instance of RoutingSingleCmdUsecase.
    """
    return RoutingSingleCmdUsecase(SIngleRoutingCmdRepositoryImpl())

def single_routing_query_usecase_factory():
    """
    Factory function that creates an instance of RoutingSingleQueryUsecase.

    Returns:
        RoutingSingleQueryUsecase: An instance of RoutingSingleQueryUsecase.
    """
    return RoutingSingleQueryUsecase(RoutingSingleRepositoryImpl())