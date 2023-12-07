from datetime import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

from chalicelib.dddpy.routings_multis_urls.infrastructure.routings_multis_urls import (
    DBRoutingMultiUrl
)


class RoutingMultiUrl:
    '''A class representing a routing multi URL.

    Attributes:
        id (Optional[int]): The ID of the routing multi URL.
        url (str): The URL of the routing multi URL.
        domain (str): The domain of the routing multi URL.
        order (int): The order of the routing multi URL.
        routing_multi_id (int): The ID of the routing multi.
        created_at (datetime): The creation date and time of the routing multi URL.
        updated_at (datetime): The last update date and time of the routing multi URL.
    '''

    def __init__(
        self,
        url: str,
        domain: str,
        order: int,
        created_at: datetime,
        updated_at: datetime,
        routing_multi_id: int,
        id: Optional[int] = None,
    ) -> None:
        self.id = id
        self.url = url
        self.domain = domain
        self.order = order
        self.routing_multi_id = routing_multi_id
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def from_db(
        cls: Type["RoutingMultiUrl"], db_routing_multi: DBRoutingMultiUrl
    ) -> "RoutingMultiUrl":
        '''Create a RoutingMultiUrl object from a DBRoutingMultiUrl object.

        Args:
            db_routing_multi (DBRoutingMultiUrl): The DBRoutingMultiUrl object.

        Returns:
            RoutingMultiUrl: The created RoutingMultiUrl object.
        '''
        return cls(
            id=db_routing_multi.id,
            order=db_routing_multi.order,
            url=db_routing_multi.url,
            domain=db_routing_multi.domain,
            routing_multi_id=db_routing_multi.routing_multi_id,
            created_at=db_routing_multi.created_at,
            updated_at=db_routing_multi.updated_at,
        )

    @classmethod
    def to_db(cls, routing_multi: "RoutingMultiUrl") -> DBRoutingMultiUrl:
        '''Convert a RoutingMultiUrl object to a DBRoutingMultiUrl object.

        Args:
            routing_multi (RoutingMultiUrl): The RoutingMultiUrl object.

        Returns:
            DBRoutingMultiUrl: The converted DBRoutingMultiUrl object.
        '''
        return DBRoutingMultiUrl(
            id=routing_multi.id,
            order=routing_multi.order,
            url=routing_multi.url,
            domain=routing_multi.domain,
            routing_multi_id=routing_multi.routing_multi_id,
            created_at=routing_multi.created_at,
            updated_at=routing_multi.updated_at,
        )

    def to_dict(self) -> Dict[str, Any]:
        '''Convert the RoutingMultiUrl object to a dictionary.

        Returns:
            Dict[str, Any]: The dictionary representation of the RoutingMultiUrl object.
        '''
        return {
            "id": self.id,
            "url": self.url,
            "domain": self.domain,
            "order": self.order,
            "routing_multi_id": self.routing_multi_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
