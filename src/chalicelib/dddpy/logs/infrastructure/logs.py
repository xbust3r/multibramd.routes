
from sqlalchemy import Column, String, Integer, ForeignKey, BigInteger, DateTime, JSON, Boolean
from sqlalchemy.orm import relationship

from chalicelib.dddpy.shared.mysql.base import Base

class DBLogs(Base):
    """
    This class represents the database table 'atalaya_logs' which stores logs information.
    """

    __tablename__="atalaya_logs"
    
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    response = Column(JSON, nullable=False)
    status=Column(Boolean, nullable=False)
    ip=Column(String(120), nullable=False)
    brand_id=Column(BigInteger, nullable=False)
    language=Column(String(5), nullable=False)
    created_at=Column(DateTime, nullable=False)
    updated_at=Column(DateTime, nullable=False)
    
    