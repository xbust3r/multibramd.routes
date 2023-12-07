from sqlalchemy import Column, Integer, BigInteger, DateTime, String, JSON, ForeignKey
from sqlalchemy.orm import relationship

from chalicelib.dddpy.shared.mysql.base import Base


class DBRoutingMultiUrl(Base):
    """
    Represents a database model for routing multi URLs.

    Attributes:
        id (BigInteger): The primary key of the model.
        order (Integer): The order of the URL.
        url (String): The URL.
        domain (String): The domain of the URL.
        routing_multi_id (BigInteger): The foreign key referencing the routing multi model.
        created_at (DateTime): The creation timestamp of the model.
        updated_at (DateTime): The last update timestamp of the model.
    """

    __tablename__ = "atalaya_routing_multi_urls"
    
    id = Column(BigInteger, primary_key=True, index=True)
    order = Column(Integer, nullable=False)
    url = Column(String(220), nullable=False)
    domain = Column(String(60), nullable=False)
    routing_multi_id = Column(BigInteger, ForeignKey("atalaya_routing_multi.id"))
    created_at = Column(DateTime)
    updated_at = Column(DateTime)