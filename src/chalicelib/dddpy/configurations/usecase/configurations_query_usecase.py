
from chalicelib.dddpy.configurations.domain.configurations_repository import (
    ConfigurationRepository,
)
from chalicelib.dddpy.configurations.usecase.configurations_query_schema import CheckDuplicatedConfigurationSchema

class ConfigurationQueryUsecase:
    """
    This class represents the use case for querying configurations.
    """

    def __init__(self, configuration_repository: ConfigurationRepository) -> None:
        """
        Initializes a new instance of the ConfigurationQueryUsecase class.

        Args:
            configuration_repository (ConfigurationRepository): The repository for configurations.
        """
        self.configuration_repository=configuration_repository
    
    def all(self):
        """
        Retrieves all configurations.

        Returns:
            List[Configuration]: A list of configurations.
        """
        return self.configuration_repository.all()
    
    def check_duplicated(self, configuration: CheckDuplicatedConfigurationSchema) -> bool:
        """
        Checks if a configuration is duplicated.

        Args:
            configuration (CheckDuplicatedConfigurationSchema): The configuration to check.

        Returns:
            bool: True if the configuration is duplicated, False otherwise.
        """
        return self.configuration_repository.check_duplicated(configuration)
    
    
    def find_configuration(self, configuration: CheckDuplicatedConfigurationSchema):
        """
        Finds a configuration.

        Args:
            configuration (CheckDuplicatedConfigurationSchema): The configuration to find.

        Returns:
            Configuration: The found configuration.
        """
        return self.configuration_repository.find_configuration(configuration)