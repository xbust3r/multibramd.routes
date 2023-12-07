from chalicelib.dddpy.shared.mysql.base import SessionLocal
from chalicelib.dddpy.routings_multis.domain.routings_multis import RoutingMulti
from chalicelib.dddpy.routings_multis.domain.routings_multis_repository import RoutingMultiRepository
from chalicelib.dddpy.routings_multis.infrastructure.routings_multis import DBRoutingMulti
from chalicelib.dddpy.shared.mysql.session_manager import session_scope

class RoutingMultiQueryRepositoryImpl(RoutingMultiRepository):
    """
    This class represents the implementation of the RoutingMultiRepository interface
    for querying RoutingMulti entities from the database.
    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the RoutingMultiQueryRepositoryImpl class.
        """
        self.session = SessionLocal()

    def find_by_id(self, id: int) -> RoutingMulti:
        """
        Finds a RoutingMulti entity by its ID.

        Args:
            id (int): The ID of the RoutingMulti entity.

        Returns:
            RoutingMulti: The found RoutingMulti entity.
        """
        with session_scope() as session:
            routing_multi = session.query(DBRoutingMulti).filter(DBRoutingMulti.id == id).first()
            return RoutingMulti.from_db(routing_multi)

    def find_by_configuration_id(self, configuration_id: int) -> RoutingMulti:
        """
        Finds a RoutingMulti entity by its configuration ID.

        Args:
            configuration_id (int): The configuration ID of the RoutingMulti entity.

        Returns:
            RoutingMulti: The found RoutingMulti entity.
        """
        with session_scope() as session:
            routing_multi = session.query(DBRoutingMulti).filter(DBRoutingMulti.configuration_id == configuration_id).first()
            return RoutingMulti.from_db(routing_multi)