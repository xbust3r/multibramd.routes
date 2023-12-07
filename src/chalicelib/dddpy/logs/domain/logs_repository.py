
from chalicelib.dddpy.logs.usecase.logs_cmd_schema import CreateLogSchema

class LogRepository:
    """
    This class represents a repository for logs in a domain.
    """

    def all(self):
        """
        Retrieves all logs from the repository.

        Returns:
            List[Log]: A list of logs.
        """
        raise NotImplementedError
    
    def create(self, data: CreateLogSchema):
        """
        Creates a new log in the repository.

        Args:
            data (CreateLogSchema): The data for the new log.

        Returns:
            Log: The created log.
        """
        raise NotImplementedError
    
    def find_by_id(self, id: int):
        """
        Finds a log in the repository by its ID.

        Args:
            id (int): The ID of the log to find.

        Returns:
            Log: The found log.
        """
        raise NotImplementedError
    
    def send_to_sqs(self, data: CreateLogSchema):
        """
        Sends a log to an SQS queue.

        Args:
            data (CreateLogSchema): The data of the log to send.
        """
        raise NotImplementedError