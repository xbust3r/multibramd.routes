from contextlib import contextmanager
from chalicelib.dddpy.shared.mysql.base import SessionLocal
from chalicelib.dddpy.routings_multis_urls.domain.routings_multis_urls import RoutingMultiUrl
from chalicelib.dddpy.routings_multis_urls.domain.routings_multis_urls_repository import RoutingMultiUrlRepository
from chalicelib.dddpy.routings_multis_urls.infrastructure.routings_multis_urls import DBRoutingMultiUrl
from chalicelib.dddpy.shared.mysql.session_manager import session_scope

class RoutingMultiUrlQueryRepositoryImpl(RoutingMultiUrlRepository):
    """
    This class implements the RoutingMultiUrlRepository interface and provides methods to query routing multi URLs from the database.
    """

    def __init__(self) -> None:
        self.session = SessionLocal()

    def find_by_id(self, id: int) -> RoutingMultiUrl:
        """
        Find a routing multi URL by its ID.

        Args:
            id (int): The ID of the routing multi URL.

        Returns:
            RoutingMultiUrl: The found routing multi URL.

        """
        with session_scope() as session:
            routing_multi_url = (
                session.query(DBRoutingMultiUrl)
                .filter(DBRoutingMultiUrl.id == id)
                .first()
            )

            return RoutingMultiUrl.from_db(routing_multi_url)

    def find_by_routing_multi_id(self, routing_multi_id: int) -> RoutingMultiUrl:
        """
        Find a routing multi URL by its routing multi ID.

        Args:
            routing_multi_id (int): The routing multi ID.

        Returns:
            RoutingMultiUrl: The found routing multi URL.

        """
        with session_scope() as session:
            routing_multi_url = (
                session.query(DBRoutingMultiUrl)
                .filter(DBRoutingMultiUrl.routing_multi_id == routing_multi_id)
                .first()
            )

            return RoutingMultiUrl.from_db(routing_multi_url)

    def find_by_routing_multi_id_and_order(
        self, routing_multi_id: int, order: int
    ) -> RoutingMultiUrl:
        """
        Find a routing multi URL by its routing multi ID and order.

        Args:
            routing_multi_id (int): The routing multi ID.
            order (int): The order of the routing multi URL.

        Returns:
            RoutingMultiUrl: The found routing multi URL.

        """
        with session_scope() as session:
            routing_multi_url = (
                session.query(DBRoutingMultiUrl)
                .filter(DBRoutingMultiUrl.routing_multi_id == routing_multi_id)
                .filter(DBRoutingMultiUrl.order == order)
                .first()
            )

            return RoutingMultiUrl.from_db(routing_multi_url)

