
from chalicelib.dddpy.shared.mysql.base import SessionLocal
from chalicelib.dddpy.configurations.domain.configurations_repository import ConfigurationRepository
from chalicelib.dddpy.configurations.infrastructure.configurations import DBConfiguration
from chalicelib.dddpy.configurations.usecase.configurations_cmd_schema import CreateConfigurationSchema, UpdateConfigurationSchema
from chalicelib.dddpy.configurations.domain.configurations import Configuration
from chalicelib.dddpy.shared.timezone import Timezone
from chalicelib.dddpy.shared.mysql.session_manager import session_scope

class ConfigurationCmdRepositoryImpl(ConfigurationRepository):
    """
    Implementation of the ConfigurationRepository interface for command operations.
    This repository is responsible for creating and updating configurations in the database.
    """

    def __init__(self):
        self.session = SessionLocal()

    def create(self, configuration: CreateConfigurationSchema) -> DBConfiguration:
        """
        Create a new configuration in the database.

        Args:
            configuration (CreateConfigurationSchema): The configuration data.

        Returns:
            DBConfiguration: The created configuration.
        """
        with session_scope() as session:
            today = Timezone.get_datetime()
            db_configuration = DBConfiguration(
                title=configuration.title,
                language=configuration.language,
                insurance=configuration.insurance,
                device=configuration.device,
                media=configuration.media,
                state=configuration.state,
                type=configuration.type,
                brand_id=configuration.brand_id,
                brand=configuration.brand,
                system=configuration.system,
                created_at=today,
                updated_at=today,
            )
            self.session.add(db_configuration)
            self.session.commit()
            self.session.refresh(db_configuration)
            return Configuration.from_db(db_configuration)

    def update(self, configuration: UpdateConfigurationSchema) -> DBConfiguration:
        """
        Update an existing configuration in the database.

        Args:
            configuration (UpdateConfigurationSchema): The updated configuration data.

        Returns:
            DBConfiguration: The updated configuration.
        """
        with session_scope() as session:
            db_configuration = (
                session.query(DBConfiguration)
                .filter(DBConfiguration.id == configuration.id)
                .first()
            )
            if not db_configuration:
                return None
            
            today = Timezone.get_datetime()
            db_configuration.language = configuration.language
            db_configuration.insurance = configuration.insurance
            db_configuration.device = configuration.device
            db_configuration.media = configuration.media
            db_configuration.state = configuration.state
            db_configuration.type = configuration.type
            db_configuration.brand_id = configuration.brand_id
            db_configuration.brand = configuration.brand
            db_configuration.updated_at = today
            session.commit()
            session.refresh(db_configuration)
            
            return Configuration.from_db(db_configuration)
