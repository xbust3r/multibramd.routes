from chalicelib.dddpy.logs.domain.logs_repository import LogRepository
from chalicelib.dddpy.logs.usecase.logs_cmd_schema import CreateLogSchema

class LogCmdUsecase:
    """
    This class represents the use case for creating logs.
    """

    def __init__(self, repository: LogRepository) -> None:
        """
        Initializes a new instance of the LogCmdUsecase class.

        Args:
            repository (LogRepository): The repository for logs.
        """
        self.repository = repository
        
    def create(self, data: CreateLogSchema):
        """
        Creates a new log.

        Args:
            data (CreateLogSchema): The data for creating the log.

        Returns:
            The created log.
        """
        return self.repository.create(data)