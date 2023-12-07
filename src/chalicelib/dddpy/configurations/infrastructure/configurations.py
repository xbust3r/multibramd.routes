
"""
This file contains the definition of the DBConfiguration class and its corresponding database table.

The DBConfiguration class inherits from the Base class, which is imported from chalicelib.dddpy.shared.mysql.base module.
The table name for this class is "atalaya_configuration".

Attributes:
    id (BigInteger): The primary key of the table, auto-incremented.
    title (String): The title of the configuration.
    language (String): The language of the configuration.
    insurance (String): The insurance of the configuration.
    device (String): The device of the configuration.
    media (String): The media of the configuration.
    state (String): The state of the configuration.
    type (Integer): The type of the configuration.
    brand_id (BigInteger): The foreign key referencing the id column of the "atalaya_brands" table.
    brand (String): The brand of the configuration.
    system (String): The system of the configuration.
    created_at (DateTime): The timestamp when the configuration was created.
    updated_at (DateTime): The timestamp when the configuration was last updated.
"""
from sqlalchemy import Column, String, Integer, ForeignKey, BigInteger, DateTime, Boolean
from sqlalchemy.orm import relationship
from chalicelib.dddpy.shared.mysql.base import Base

class DBConfiguration(Base):
    __tablename__="atalaya_configuration"
    
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    title=Column(String, nullable=False)
    language=Column(String, nullable=False)
    insurance=Column(String, nullable=False)
    device=Column(String, nullable=False)
    media=Column(String, nullable=False)
    state=Column(String, nullable=False)
    type=Column(Integer, nullable=False)
    brand_id=Column(BigInteger, ForeignKey("atalaya_brands.id"), nullable=True)
    brand=Column(String, nullable=False)
    system=Column(String, nullable=False)
    created_at=Column(DateTime, nullable=False)
    updated_at=Column(DateTime, nullable=False)
    