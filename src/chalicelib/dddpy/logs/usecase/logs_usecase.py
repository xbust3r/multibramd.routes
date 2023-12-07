from chalicelib.dddpy.logs.usecase.logs_cmd_schema import CreateLogSchema
from chalicelib.dddpy.logs.usecase.logs_factory import log_cmd_usecase_factory, log_query_usecase_factory, log_sqs_cmd_usecase_factory
from chalicelib.dddpy.logs.domain.logs_exception import LogsNotFoundError
from chalicelib.dddpy.logs.domain.logs_success import LogsSucessMessages
from chalicelib.dddpy.shared.schemas.response_schema import (
    ResponseSuccessSchema,
    ResponseErrorSchema,
)
from chalicelib.dddpy.logs.usecase.log_sqs_cmd_usecase import LogSqsCmdUsecase
import logging

class LogUsecase:
    """
    This class represents the use case for logs.
    It provides methods for creating logs, retrieving all logs, and sending logs to SQS.
    """

    def __init__(self):
        """
        Initializes the LogUsecase class.
        """
        self.log_cmd_usecase = log_cmd_usecase_factory()
        self.log_query_usecase = log_query_usecase_factory()
        self.log_sqs_cmd_usecase = log_sqs_cmd_usecase_factory()
        
    def create(self, data: CreateLogSchema):
        """
        Creates a new log.

        Args:
            data (CreateLogSchema): The data for creating the log.

        Returns:
            ResponseSuccessSchema: The success response with the created log data.

        Raises:
            Exception: If an error occurs during the creation of the log.
        """
        try:
            logging.info("create")
            create = self.log_cmd_usecase.create(data)
            
            success = ResponseSuccessSchema(
                message=LogsSucessMessages.LOG_CREATED,
                data=create.to_dict(),
            )
            return success
        
        except Exception as e:
            raise e
        
    def all(self):
        """
        Retrieves all logs.

        Returns:
            ResponseSuccessSchema: The success response with the list of logs.

        Raises:
            Exception: If an error occurs during the retrieval of the logs.
            LogsNotFoundError: If no logs are found.
        """
        try:
            logs = self.log_query_usecase.all()
            print(logs)
            if logs is None or len(logs) == 0:
                raise LogsNotFoundError
            
            data_dict = [l.to_dict() for l in logs]   
            success = ResponseSuccessSchema(
                message=LogsSucessMessages.LOGS_FOUND,
                data=data_dict
            )
            return success
        
        except Exception as e:
            raise e
        
    def send_to_sqs(self, data: CreateLogSchema):
        """
        Sends a log to SQS.

        Args:
            data (CreateLogSchema): The data of the log to be sent.

        Returns:
            bool: True if the log is successfully sent to SQS.

        Raises:
            Exception: If an error occurs during the sending of the log.
        """
        try:
            logging.info("send_to_sqs")
            logging.info(data)
            return self.log_sqs_cmd_usecase.send_to_sqs(data)
        
        except Exception as e:
            raise e