from sqlalchemy import Column, String, Integer, ForeignKey, BigInteger, DateTime
from sqlalchemy.orm import relationship

from chalicelib.dddpy.shared.mysql.base import Base

class DBBrands(Base):
    """
    Represents the database table 'atalaya_brands' for storing brand information.
    """

    __tablename__ = "atalaya_brands"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    brand = Column(String, nullable=False)
    brand_code = Column(String, nullable=False)
    description = Column(String, nullable=False)
    brand_id = Column(BigInteger, nullable=True)
    
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False)
    