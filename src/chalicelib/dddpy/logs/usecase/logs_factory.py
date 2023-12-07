"""
This module contains factory functions for creating instances of use case classes related to logging.

The factory functions provided in this module are:
- log_cmd_usecase_factory: Creates an instance of LogCmdUsecase class.
- log_query_usecase_factory: Creates an instance of LogQueryUsecase class.
- log_sqs_cmd_usecase_factory: Creates an instance of LogSqsCmdUsecase class.
"""

from chalicelib.dddpy.logs.usecase.logs_cmd_usecase import LogCmdUsecase
from chalicelib.dddpy.logs.infrastructure.logs_cmd_repository import LogCmdRepositoryImpl

from chalicelib.dddpy.logs.usecase.logs_query_usecase import LogQueryUsecase
from chalicelib.dddpy.logs.infrastructure.logs_query_repository import LogQueryRepositoryImpl

from chalicelib.dddpy.logs.usecase.log_sqs_cmd_usecase import LogSqsCmdUsecase
from chalicelib.dddpy.logs.infrastructure.log_sqs_cmd_repository import LogSqsCmdRepositoryImpl


def log_cmd_usecase_factory():
    """
    Factory function for creating an instance of LogCmdUsecase class.

    Returns:
        LogCmdUsecase: An instance of LogCmdUsecase class.
    """
    log_cmd_repository = LogCmdRepositoryImpl()
    return LogCmdUsecase(log_cmd_repository)


def log_query_usecase_factory():
    """
    Factory function for creating an instance of LogQueryUsecase class.

    Returns:
        LogQueryUsecase: An instance of LogQueryUsecase class.
    """
    log_query_repository = LogQueryRepositoryImpl()
    return LogQueryUsecase(log_query_repository)


def log_sqs_cmd_usecase_factory():
    """
    Factory function for creating an instance of LogSqsCmdUsecase class.

    Returns:
        LogSqsCmdUsecase: An instance of LogSqsCmdUsecase class.
    """
    log_sqs_cmd_repository = LogSqsCmdRepositoryImpl()
    return LogSqsCmdUsecase(log_sqs_cmd_repository)