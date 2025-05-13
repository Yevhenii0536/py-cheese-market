from enum import StrEnum, auto

from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey
from sqlalchemy.orm import relationship

from db.engine import Base


class PackagingType(StrEnum):
    BOX = auto()
    BAG = auto()
    WRAP = auto()
    WEIGHT = auto()
    OTHER = auto()


class CheeseType(Base):
    __tablename__ = "cheese_type"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, unique=True)
    description = Column(String(511), nullable=True)

    cheeses = relationship("Cheese", back_populates="cheese_type")



class Cheese(Base):
    __tablename__ = "cheese"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, unique=True)
    price = Column(Float, nullable=False)
    packaging_type = Column(Enum(PackagingType), nullable=False)

    cheese_type_id = Column(
        Integer,
        ForeignKey("cheese_type.id", name="fk_cheese_cheese_type_id"),
        nullable=False
    )
    cheese_type = relationship("CheeseType", back_populates="cheeses")
    
