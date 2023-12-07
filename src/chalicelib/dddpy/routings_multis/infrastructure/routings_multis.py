from sqlalchemy import Column, Integer, BigInteger, DateTime, String, JSON, ForeignKey
from sqlalchemy.orm import relationship

from chalicelib.dddpy.shared.mysql.base import Base


class DBRoutingMulti(Base):
    """
    Represents a database model for the 'atalaya_routing_multi' table.
    """

    __tablename__ = "atalaya_routing_multi"

    id = Column(BigInteger, primary_key=True, index=True)
    current = Column(Integer, nullable=False)
    total = Column(Integer, nullable=False)
    variables = Column(JSON, nullable=False)
    configuration_id = Column(BigInteger, ForeignKey("atalaya_configuration.id"), nullable=False)
    brand_id = Column(BigInteger, ForeignKey("atalaya_brands.id"), nullable=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)