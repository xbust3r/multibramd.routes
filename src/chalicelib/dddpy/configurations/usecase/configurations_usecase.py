
from chalicelib.dddpy.configurations.domain.configurations_exception import (
    ConfigurationAlreadyExistsError,
    ConfigurationNotFoundError,
    ConfigurationsNotFoundError,
)
from chalicelib.dddpy.configurations.usecase.configurations_cmd_schema import (
    CreateConfigurationSchema,
    UpdateConfigurationSchema,
)
from chalicelib.dddpy.configurations.usecase.configurations_query_schema import (
    CheckDuplicatedConfigurationSchema,
    FindConfigurationSchema,
)
from chalicelib.dddpy.configurations.domain.configurations_success import (
    ConfigurationSuccessMessages,
)
from chalicelib.dddpy.configurations.usecase.configurations_factory import (
    configuration_cmd_usecase_factory,
    configuration_query_usecase_factory,
)
from chalicelib.dddpy.shared.schemas.response_schema import (
    ResponseSuccessSchema,
    ResponseErrorSchema,
)
import logging


class ConfigurationUsecase:
    """
    This class represents the use case for managing configurations.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the ConfigurationUsecase class.
        """
        self.configuration_cmd_usecase = configuration_cmd_usecase_factory()
        self.configuration_query_usecase = configuration_query_usecase_factory()

    def create(self, configuration: CreateConfigurationSchema):
        """
        Creates a new configuration.

        Args:
            configuration (CreateConfigurationSchema): The configuration data.

        Returns:
            ResponseSuccessSchema: The response schema containing the success message and the created configuration data.

        Raises:
            ConfigurationAlreadyExistsError: If the configuration already exists.
            Exception: If an error occurs during the creation process.
        """
        try:
            configuration = self.configuration_cmd_usecase.create(configuration)
            return ResponseSuccessSchema(
                message=ConfigurationSuccessMessages.CREATE_SUCCESS,
                data=configuration.to_dict(),
            )
        except ConfigurationAlreadyExistsError as e:
            raise ConfigurationAlreadyExistsError
        except Exception as e:
            raise e

    def all(self):
        """
        Retrieves all configurations.

        Returns:
            dict: The response schema containing the success message and the list of configurations.

        Raises:
            ConfigurationsNotFoundError: If no configurations are found.
            Exception: If an error occurs during the retrieval process.
        """
        configurations = self.configuration_query_usecase.all()

        if configurations is None:
            raise ConfigurationsNotFoundError
        try:
            data_configurations = [
                configuration.to_dict() for configuration in configurations
            ]
            response_schema = ResponseSuccessSchema(
                message=ConfigurationSuccessMessages.ALL_SUCCESS,
                data=data_configurations,
            )
            return response_schema.dict()

        except Exception as e:
            raise e

    def check_duplicated(self, configuration: CheckDuplicatedConfigurationSchema):
        """
        Checks if a configuration is duplicated.

        Args:
            configuration (CheckDuplicatedConfigurationSchema): The configuration data to check.

        Returns:
            ResponseSuccessSchema: The response schema containing the success message and the duplicated flag.

        Raises:
            Exception: If an error occurs during the check process.
        """
        try:
            duplicated = self.configuration_query_usecase.check_duplicated(
                configuration
            )
            return ResponseSuccessSchema(
                message=ConfigurationSuccessMessages.CHECK_DUPLICATED_SUCCESS,
                data=duplicated,
            )
        except Exception as e:
            raise e

    def find_configuration(self, configuration: FindConfigurationSchema):
        """
        Finds a configuration.

        Args:
            configuration (FindConfigurationSchema): The configuration data to find.

        Returns:
            ResponseSuccessSchema: The response schema containing the success message and the found configuration data.

        Raises:
            ConfigurationNotFoundError: If the configuration is not found.
            Exception: If an error occurs during the find process.
        """
        try:
            configuration = self.configuration_query_usecase.find_configuration(
                configuration
            )
            logging.info(configuration)
            if configuration is None:
                raise ConfigurationNotFoundError
            return ResponseSuccessSchema(
                message=ConfigurationSuccessMessages.FIND_CONFIGURATION_SUCCESS,
                data=configuration.to_dict(),
            )
        except Exception as e:
            raise e
