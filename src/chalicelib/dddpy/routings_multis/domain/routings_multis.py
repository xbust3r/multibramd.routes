from datetime import datetime
from typing import Any, Dict, List, Optional, Type, TypeVar, Union

from chalicelib.dddpy.routings_multis.infrastructure.routings_multis import DBRoutingMulti

class RoutingMulti:
    """
    Represents a routing multi object.
    """

    def __init__(self
        , current: int
        , total: int
        , variables: Dict[str, Any]
        , configuration_id: int
        , brand_id: Optional[int]
        , created_at: datetime
        , updated_at: datetime
        , id: Optional[int] = None
    ) -> None:
        """
        Initializes a new instance of the RoutingMulti class.

        Args:
            current (int): The current value.
            total (int): The total value.
            variables (Dict[str, Any]): The variables.
            configuration_id (int): The configuration ID.
            brand_id (Optional[int]): The brand ID.
            created_at (datetime): The creation date and time.
            updated_at (datetime): The update date and time.
            id (Optional[int], optional): The ID. Defaults to None.
        """
        self.id = id
        self.current = current
        self.total = total
        self.variables = variables
        self.configuration_id = configuration_id
        self.brand_id = brand_id
        self.created_at = created_at
        self.updated_at = updated_at             

    @classmethod
    def from_db(
        cls: Type["RoutingMulti"], db_routing_multi: DBRoutingMulti
    ) -> "RoutingMulti":
        """
        Creates a RoutingMulti instance from a DBRoutingMulti instance.

        Args:
            db_routing_multi (DBRoutingMulti): The DBRoutingMulti instance.

        Returns:
            RoutingMulti: The created RoutingMulti instance.
        """
        return cls(
            id=db_routing_multi.id,
            current=db_routing_multi.current,
            total=db_routing_multi.total,
            variables=db_routing_multi.variables,
            configuration_id=db_routing_multi.configuration_id,
            brand_id=db_routing_multi.brand_id,
            created_at=db_routing_multi.created_at,
            updated_at=db_routing_multi.updated_at,
        )
        
    @classmethod
    def to_db(cls, routing_multi: "RoutingMulti") -> DBRoutingMulti:  
        """
        Converts a RoutingMulti instance to a DBRoutingMulti instance.

        Args:
            routing_multi (RoutingMulti): The RoutingMulti instance.

        Returns:
            DBRoutingMulti: The converted DBRoutingMulti instance.
        """
        return DBRoutingMulti(
            id=routing_multi.id,
            current=routing_multi.current,
            total=routing_multi.total,
            variables=routing_multi.variables,
            configuration_id=routing_multi.configuration_id,
            brand_id=routing_multi.brand_id,
            created_at=routing_multi.created_at,
            updated_at=routing_multi.updated_at,
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the RoutingMulti instance to a dictionary.

        Returns:
            Dict[str, Any]: The dictionary representation of the RoutingMulti instance.
        """
        return {
            "id": self.id,
            "current": self.current,
            "total": self.total,
            "variables": self.variables,
            "configuration_id": self.configuration_id,
            "brand_id": self.brand_id,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }