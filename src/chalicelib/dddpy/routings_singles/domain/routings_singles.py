from datetime import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

from chalicelib.dddpy.routings_singles.infrastructure.routings_singles import (
    DBRoutingSingle,
)

class RoutingSingle:
    '''Represents a single routing entity.'''
    def __init__(
        self,
        url: str,
        domain: str,
        variables: Dict[str, Any],
        configuration_id: int,
        brand_id: Optional[int],
        created_at: datetime,
        updated_at: datetime,
        id: Optional[int] = None,
    ) -> None:
        '''
        Initializes a new instance of the RoutingSingle class.

        Args:
            url (str): The URL of the routing.
            domain (str): The domain of the routing.
            variables (Dict[str, Any]): The variables associated with the routing.
            configuration_id (int): The ID of the configuration associated with the routing.
            brand_id (Optional[int]): The ID of the brand associated with the routing.
            created_at (datetime): The creation date and time of the routing.
            updated_at (datetime): The last update date and time of the routing.
            id (Optional[int], optional): The ID of the routing. Defaults to None.
        '''
        self.id = id
        self.url = url
        self.domain = domain
        self.variables = variables
        self.configuration_id = configuration_id
        self.brand_id = brand_id
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def from_db(
        cls: Type["RoutingSingle"], db_routing_single: DBRoutingSingle
    ) -> "RoutingSingle":
        '''
        Creates a RoutingSingle instance from a DBRoutingSingle instance.

        Args:
            db_routing_single (DBRoutingSingle): The DBRoutingSingle instance.

        Returns:
            RoutingSingle: The created RoutingSingle instance.
        '''
        return cls(
            id=db_routing_single.id,
            url=db_routing_single.url,
            domain=db_routing_single.domain,
            variables=db_routing_single.variables,
            configuration_id=db_routing_single.configuration_id,
            brand_id=db_routing_single.brand_id,
            created_at=db_routing_single.created_at,
            updated_at=db_routing_single.updated_at,
        )

    @classmethod
    def to_db(cls, routing_single: "RoutingSingle") -> DBRoutingSingle:  
        '''
        Converts a RoutingSingle instance to a DBRoutingSingle instance.

        Args:
            routing_single (RoutingSingle): The RoutingSingle instance.

        Returns:
            DBRoutingSingle: The converted DBRoutingSingle instance.
        '''
        return DBRoutingSingle(
            id=routing_single.id,
            url=routing_single.url,
            domain=routing_single.domain,
            variables=routing_single.variables,
            configuration_id=routing_single.configuration_id,
            brand_id=routing_single.brand_id,
            created_at=routing_single.created_at,
            updated_at=routing_single.updated_at,
        )

    def to_dict(self) -> Dict[str, Any]:
        '''
        Converts the RoutingSingle instance to a dictionary.

        Returns:
            Dict[str, Any]: The dictionary representation of the RoutingSingle instance.
        '''
        return {
            "id": self.id,
            "url": self.url,
            "domain": self.domain,
            "variables": self.variables,
            "configuration_id": self.configuration_id,
            "brand_id": self.brand_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }
