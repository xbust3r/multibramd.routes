from chalicelib.dddpy.logs.domain.logs_repository import LogRepository
from chalicelib.dddpy.logs.usecase.logs_cmd_schema import CreateLogSchema

class LogSqsCmdUsecase:
    """
    This class represents a use case for sending logs to SQS.
    """

    def __init__(self, log_repository: LogRepository):
        """
        Initializes a new instance of the LogSqsCmdUsecase class.

        Parameters:
        - log_repository (LogRepository): The repository for logs.
        """
        self.log_repository = log_repository
    
    def send_to_sqs(self, data: CreateLogSchema):
        """
        Sends the log data to SQS.

        Parameters:
        - data (CreateLogSchema): The log data to be sent.

        Returns:
        - bool: True if the log data was successfully sent, False otherwise.
        """
        return self.log_repository.send_to_sqs(data)