from chalicelib.dddpy.logs.domain.logs_repository import LogRepository

class LogQueryUsecase:
    """
    This class represents a use case for querying logs.
    """

    def __init__(self, log_repository: LogRepository) -> None:
        """
        Initializes a new instance of the LogQueryUsecase class.

        Parameters:
        - log_repository (LogRepository): The repository for accessing logs.
        """
        self.log_repository=log_repository
        
    def all(self):
        """
        Retrieves all logs.

        Returns:
        - list: A list of logs.
        """
        return self.log_repository.all()