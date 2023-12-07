
from chalicelib.dddpy.configurations.usecase.configurations_cmd_usecase import ConfigurationCmdUsecase
from chalicelib.dddpy.configurations.infrastructure.configurations_cmd_repository import ConfigurationCmdRepositoryImpl
from chalicelib.dddpy.configurations.usecase.configurations_query_usecase import ConfigurationQueryUsecase
from chalicelib.dddpy.configurations.infrastructure.configurations_query_repository import ConfigurationQueryRepositoryImpl

def configuration_cmd_usecase_factory() -> ConfigurationCmdUsecase:
    """
    Factory function to create an instance of ConfigurationCmdUsecase.

    Returns:
        ConfigurationCmdUsecase: An instance of ConfigurationCmdUsecase.
    """
    return ConfigurationCmdUsecase(ConfigurationCmdRepositoryImpl())

def configuration_query_usecase_factory() -> ConfigurationQueryUsecase:
    """
    Factory function to create an instance of ConfigurationQueryUsecase.

    Returns:
        ConfigurationQueryUsecase: An instance of ConfigurationQueryUsecase.
    """
    return ConfigurationQueryUsecase(ConfigurationQueryRepositoryImpl())
