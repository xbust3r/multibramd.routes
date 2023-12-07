
from chalicelib.dddpy.configurations.infrastructure.configurations import DBConfiguration
from chalicelib.dddpy.configurations.usecase.configurations_cmd_schema import CreateConfigurationSchema, UpdateConfigurationSchema
from chalicelib.dddpy.configurations.usecase.configurations_query_schema import CheckDuplicatedConfigurationSchema, FindConfigurationSchema

class ConfigurationRepository:
    """
    Repository class for managing configurations.
    """

    def create(self, configuration: CreateConfigurationSchema) -> DBConfiguration:
        """
        Create a new configuration.

        Args:
            configuration (CreateConfigurationSchema): The configuration data.

        Returns:
            DBConfiguration: The created configuration.
        """
        raise NotImplementedError()

    def update(self, configuration: UpdateConfigurationSchema) -> DBConfiguration:
        """
        Update an existing configuration.

        Args:
            configuration (UpdateConfigurationSchema): The updated configuration data.

        Returns:
            DBConfiguration: The updated configuration.
        """
        raise NotImplementedError()

    def delete(self, id: int) -> None:
        """
        Delete a configuration by ID.

        Args:
            id (int): The ID of the configuration to delete.
        """
        raise NotImplementedError()

    def all(self) -> list[DBConfiguration]:
        """
        Get all configurations.

        Returns:
            list[DBConfiguration]: A list of all configurations.
        """
        raise NotImplementedError()

    def search_by_id(self, id: int) -> DBConfiguration:
        """
        Search for a configuration by ID.

        Args:
            id (int): The ID of the configuration to search for.

        Returns:
            DBConfiguration: The found configuration.
        """
        raise NotImplementedError()

    def search_by_brand_id(self, brand_id: int) -> list[DBConfiguration]:
        """
        Search for configurations by brand ID.

        Args:
            brand_id (int): The ID of the brand to search for.

        Returns:
            list[DBConfiguration]: A list of configurations matching the brand ID.
        """
        raise NotImplementedError()

    def check_duplicated(self, configuration: CreateConfigurationSchema) -> bool:
        """
        Check if a configuration is duplicated.

        Args:
            configuration (CreateConfigurationSchema): The configuration data to check.

        Returns:
            bool: True if the configuration is duplicated, False otherwise.
        """
        raise NotImplementedError()

    def find_configuration(self, configuration: FindConfigurationSchema) -> DBConfiguration:
        """
        Find a configuration.

        Args:
            configuration (FindConfigurationSchema): The configuration data to search for.

        Returns:
            DBConfiguration: The found configuration.
        """
        raise NotImplementedError()
    