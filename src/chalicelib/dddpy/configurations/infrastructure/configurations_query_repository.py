
from chalicelib.dddpy.shared.mysql.base import SessionLocal
from chalicelib.dddpy.configurations.domain.configurations_repository import ConfigurationRepository
from chalicelib.dddpy.configurations.infrastructure.configurations import DBConfiguration
from chalicelib.dddpy.configurations.domain.configurations import Configuration
from chalicelib.dddpy.configurations.usecase.configurations_query_schema import CheckDuplicatedConfigurationSchema, FindConfigurationSchema
from chalicelib.dddpy.shared.mysql.session_manager import session_scope

class ConfigurationQueryRepositoryImpl(ConfigurationRepository):
    """
    Implementation of the ConfigurationRepository interface for querying configurations from the database.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the ConfigurationQueryRepositoryImpl class.
        """
        self.session = SessionLocal()

    def all(self) -> list[DBConfiguration]:
        """
        Retrieves all configurations from the database.

        Returns:
            A list of DBConfiguration objects representing the configurations.
        """
        with session_scope() as session:
            db_configurations = session.query(DBConfiguration).all()

            if db_configurations is None:
                return None

            data = {
                Configuration.from_db(db_configuration)
                for db_configuration in db_configurations
            }

            return data

    def check_duplicated(
        self, configuration: CheckDuplicatedConfigurationSchema
    ) -> bool:
        """
        Checks if a configuration with the same properties already exists in the database.

        Args:
            configuration: The CheckDuplicatedConfigurationSchema object representing the configuration to check.

        Returns:
            True if a duplicated configuration exists, False otherwise.
        """
        with session_scope() as session:
            db_configuration = (
                session.query(DBConfiguration)
                .filter(DBConfiguration.language == configuration.language)
                .filter(DBConfiguration.insurance == configuration.insurance)
                .filter(DBConfiguration.device == configuration.device)
                .filter(DBConfiguration.media == configuration.media)
                .filter(DBConfiguration.state == configuration.state)
                .filter(DBConfiguration.type == configuration.type)
                .filter(DBConfiguration.brand_id == configuration.brand_id)
                .first()
            )

            if db_configuration is None:
                return False

            return True

    def find_configuration(self, configuration: FindConfigurationSchema) -> DBConfiguration:
        """
        Finds a configuration in the database based on the specified properties.

        Args:
            configuration: The FindConfigurationSchema object representing the properties to search for.

        Returns:
            The DBConfiguration object representing the found configuration, or None if not found.
        """
        with session_scope() as session:
            db_configuration = (
                session.query(DBConfiguration)
                .filter(DBConfiguration.language == configuration.language)
                .filter(DBConfiguration.insurance == configuration.insurance)
                .filter(DBConfiguration.device == configuration.device)
                .filter(DBConfiguration.media == configuration.media)
                .filter(DBConfiguration.state == configuration.state)
                .filter(DBConfiguration.brand_id == configuration.brand_id)
                .first()
            )

            if db_configuration is None:
                return None
            
            return Configuration.from_db(db_configuration)

    def search_by_id(self, id: int) -> DBConfiguration:
        """
        Searches for a configuration in the database by its ID.

        Args:
            id: The ID of the configuration to search for.

        Returns:
            The DBConfiguration object representing the found configuration, or None if not found.
        """
        with session_scope() as session:
            db_configuration = (
                self.session.query(DBConfiguration).filter(DBConfiguration.id == id).first()
            )
            with session_scope() as session:
                if db_configuration is None:
                    return None

                return Configuration.from_db(db_configuration)

