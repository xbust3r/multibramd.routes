from chalicelib.dddpy.routings_multis_urls.domain.routings_multis_urls_repository import RoutingMultiUrlRepository
from chalicelib.dddpy.routings_multis_urls.usecase.routings_multis_urls_cmd_schema import (
    CreateRoutingMultiUrlSchema
)
from chalicelib.dddpy.routings_multis_urls.domain.routings_multis_urls import RoutingMultiUrl
from chalicelib.dddpy.routings_multis_urls.infrastructure.routings_multis_urls import DBRoutingMultiUrl

from chalicelib.dddpy.shared.mysql.base import SessionLocal
from chalicelib.dddpy.shared.timezone import Timezone

from chalicelib.dddpy.shared.mysql.session_manager import session_scope


class RoutingMultiUrlCmdRepositoryImpl(RoutingMultiUrlRepository):
    """
    This class implements the RoutingMultiUrlRepository interface and provides
    the functionality to create routing multi URLs in the database.

    Attributes:
        repo (SessionLocal): The database session.

    Methods:
        create(routing_multi: CreateRoutingMultiUrlSchema) -> RoutingMultiUrl:
            Creates a new routing multi URL in the database and returns the created object.
    """

    def __init__(self) -> None:
        self.repo = SessionLocal()
        
    def create(self, routing_multi: CreateRoutingMultiUrlSchema) -> RoutingMultiUrl:
        """
        Creates a new routing multi URL in the database.

        Args:
            routing_multi (CreateRoutingMultiUrlSchema): The schema containing the details of the routing multi URL.

        Returns:
            RoutingMultiUrl: The created routing multi URL object.
        """
        with session_scope() as session:
            today = Timezone.get_datetime()
            routing_multi = RoutingMultiUrl(
                id=None,
                url=routing_multi.url,
                domain=routing_multi.domain,
                order=routing_multi.order,
                routing_multi_id=routing_multi.routing_multi_id,
                created_at=today,
                updated_at=today,
            )
            new_routing_multi = RoutingMultiUrl.to_db(routing_multi)
            session.add(new_routing_multi)
            session.commit()
            session.refresh(new_routing_multi)
            
            return RoutingMultiUrl.from_db(new_routing_multi)
    