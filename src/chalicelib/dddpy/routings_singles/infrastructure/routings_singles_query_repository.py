from chalicelib.dddpy.shared.mysql.base import SessionLocal
from chalicelib.dddpy.routings_singles.domain.routings_singles_repository import RoutingSingleRepository
from chalicelib.dddpy.routings_singles.domain.routings_singles import RoutingSingle
from chalicelib.dddpy.routings_singles.infrastructure.routings_singles import DBRoutingSingle
from chalicelib.dddpy.shared.mysql.session_manager import session_scope

class RoutingSingleRepositoryImpl(RoutingSingleRepository):
    """Implementation of the RoutingSingleRepository interface for querying routing singles."""

    def __init__(self) -> None:
        """Initialize the RoutingSingleRepositoryImpl."""
        self.session = SessionLocal()

    def find_by_id(self, id: int) -> DBRoutingSingle:
        """Find a routing single by its ID.

        Args:
            id (int): The ID of the routing single.

        Returns:
            DBRoutingSingle: The routing single object if found, None otherwise.
        """
        with session_scope() as session:
            db_single = session.query(DBRoutingSingle).filter(DBRoutingSingle.id == id).first()

            if db_single is None:
                return None

            return RoutingSingle.from_db(db_single)

    def find_by_configuration_id(self, configuration_id: int) -> DBRoutingSingle:
        """Find a routing single by its configuration ID.

        Args:
            configuration_id (int): The configuration ID of the routing single.

        Returns:
            DBRoutingSingle: The routing single object if found, None otherwise.
        """
        with session_scope() as session:
            db_single = session.query(DBRoutingSingle).filter(DBRoutingSingle.configuration_id == configuration_id).first()

            if db_single is None:
                return None

            return RoutingSingle.from_db(db_single)