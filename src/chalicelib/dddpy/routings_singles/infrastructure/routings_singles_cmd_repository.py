from chalicelib.dddpy.routings_singles.domain.routings_singles import RoutingSingle
from chalicelib.dddpy.routings_singles.domain.routings_singles_repository import RoutingSingleRepository
from chalicelib.dddpy.routings_singles.infrastructure.routings_singles import DBRoutingSingle

from chalicelib.dddpy.routings_singles.usecase.routings_singles_cmd_schema import ( CreateSingleRoutingSchema, UpdateSingleRoutingSchema )

from chalicelib.dddpy.shared.mysql.base import SessionLocal
from chalicelib.dddpy.shared.timezone import Timezone

from chalicelib.dddpy.shared.mysql.session_manager import session_scope

class SIngleRoutingCmdRepositoryImpl(RoutingSingleRepository):
    """
    Implementation of the RoutingSingleRepository interface for command operations.
    """

    def __init__(self):
        """
        Initializes the SingleRoutingCmdRepositoryImpl class.
        """
        self.session = SessionLocal()

    def create(self, data: CreateSingleRoutingSchema):
        """
        Creates a new routing single.

        Args:
            data (CreateSingleRoutingSchema): The data for creating the routing single.

        Returns:
            RoutingSingle: The created routing single.
        """
        with session_scope() as session:
            today = Timezone.get_datetime()

            routing_single = RoutingSingle(
                id=None,
                url=data.url,
                domain=data.domain,
                variables=data.variables,
                configuration_id=data.configuration_id,
                brand_id=data.brand_id,
                created_at=today,
                updated_at=today,
            )
            new_routing_single = RoutingSingle.to_db(routing_single)
            session.add(new_routing_single)
            session.commit()
            session.refresh(new_routing_single)
            return RoutingSingle.from_db(new_routing_single)