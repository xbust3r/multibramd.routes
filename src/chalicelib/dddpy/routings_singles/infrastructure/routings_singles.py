from sqlalchemy import Column, Integer, BigInteger, DateTime, String, JSON, ForeignKey
from sqlalchemy.orm import relationship

from chalicelib.dddpy.shared.mysql.base import Base

class DBRoutingSingle(Base):
    """
    Represents a single routing in the database.

    Attributes:
        id (int): The unique identifier of the routing.
        url (str): The URL of the routing.
        domain (str): The domain of the routing.
        variables (dict): The variables associated with the routing.
        configuration_id (int): The ID of the configuration associated with the routing.
        brand_id (int): The ID of the brand associated with the routing (optional).
        created_at (datetime): The timestamp when the routing was created.
        updated_at (datetime): The timestamp when the routing was last updated.
    """
    __tablename__ = "atalaya_routing_single"

    id = Column(BigInteger, primary_key=True, index=True)
    url = Column(String, nullable=False)
    domain = Column(String, nullable=False)
    variables = Column(JSON, nullable=False)
    configuration_id = Column(BigInteger, ForeignKey("atalaya_configuration.id"), nullable=False)
    brand_id = Column(BigInteger, ForeignKey("atalaya_brands.id"), nullable=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)