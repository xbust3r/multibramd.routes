from chalicelib.dddpy.routings_multis.domain.routings_multis_repository import RoutingMultiRepository
from chalicelib.dddpy.routings_multis.usecase.routings_multis_cmd_schema import (
    CreateRoutingMultiSchema,
    UpdateRoutingMultiSchema,
)
from chalicelib.dddpy.routings_multis.domain.routings_multis import RoutingMulti
from chalicelib.dddpy.routings_multis.infrastructure.routings_multis import DBRoutingMulti

from chalicelib.dddpy.shared.mysql.base import SessionLocal
from chalicelib.dddpy.shared.timezone import Timezone

from chalicelib.dddpy.shared.mysql.session_manager import session_scope


class RoutingMultiCmdRepositoryImpl(RoutingMultiRepository):
    """
    Repository implementation for handling routing multi entities in the command side.
    """

    def __init__(self) -> None:
        """
        Initializes the RoutingMultiCmdRepositoryImpl object.
        """
        self.session = SessionLocal()

    def create(self, routing_multi: CreateRoutingMultiSchema):
        """
        Creates a new routing multi entity.

        Args:
            routing_multi (CreateRoutingMultiSchema): The schema containing the data for creating a routing multi.

        Returns:
            RoutingMulti: The created routing multi entity.
        """
        with session_scope() as session:
            today = Timezone.get_datetime()
            routing_multi = RoutingMulti(
                id=None,
                variables=routing_multi.variables,
                current=0,
                total=routing_multi.total,
                configuration_id=routing_multi.configuration_id,
                brand_id=routing_multi.brand_id,
                created_at=today,
                updated_at=today,
            )
            new_routing_multi = RoutingMulti.to_db(routing_multi)
            session.add(new_routing_multi)
            session.commit()
            session.refresh(new_routing_multi)

            return RoutingMulti.from_db(new_routing_multi)

    def update_current_by_id(self, id: int, current: int):
        """
        Updates the current value of a routing multi entity by its ID.

        Args:
            id (int): The ID of the routing multi entity.
            current (int): The new value for the current field.

        Returns:
            RoutingMulti: The updated routing multi entity.
        """
        with session_scope() as session:
            routing_multi = session.query(DBRoutingMulti).filter(DBRoutingMulti.id == id).first()
            routing_multi.current = current
            session.commit()

            return RoutingMulti.from_db(routing_multi)