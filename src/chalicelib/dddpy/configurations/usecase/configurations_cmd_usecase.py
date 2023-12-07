
from chalicelib.dddpy.configurations.domain.configurations_repository import ConfigurationRepository
from chalicelib.dddpy.configurations.usecase.configurations_cmd_schema import CreateConfigurationSchema, UpdateConfigurationSchema


class ConfigurationCmdUsecase:
    """
    This class represents the use case for managing configurations.
    """

    def __init__(self, configuration_repository: ConfigurationRepository):
        """
        Initializes a new instance of the ConfigurationCmdUsecase class.

        Parameters:
        - configuration_repository (ConfigurationRepository): The repository for configurations.
        """
        self.configuration_repository = configuration_repository

    def create(self, configuration: CreateConfigurationSchema):
        """
        Creates a new configuration.

        Parameters:
        - configuration (CreateConfigurationSchema): The configuration data.

        Returns:
        - The created configuration.
        """
        return self.configuration_repository.create(configuration)

    def update(self, configuration: UpdateConfigurationSchema):
        """
        Updates an existing configuration.

        Parameters:
        - configuration (UpdateConfigurationSchema): The updated configuration data.

        Returns:
        - The updated configuration.
        """
        return self.configuration_repository.update(configuration)
    