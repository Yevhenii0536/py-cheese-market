from enum import StrEnum, auto
from datetime import datetime

from sqlalchemy import String, Float, Enum, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db.engine import Base


class PackagingType(StrEnum):
    BOX = auto()
    BAG = auto()
    WRAP = auto()
    WEIGHT = auto()
    OTHER = auto()


class CheeseType(Base):
    __tablename__ = "cheese_type"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    description: Mapped[str | None] = mapped_column(String(511), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), onupdate=func.now())

    cheeses: Mapped[list["Cheese"]] = relationship("Cheese", back_populates="cheese_type")


class Cheese(Base):
    __tablename__ = "cheese"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    packaging_type: Mapped[PackagingType] = mapped_column(Enum(PackagingType), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), onupdate=func.now())

    cheese_type_id: Mapped[int] = mapped_column(
        ForeignKey("cheese_type.id", name="fk_cheese_cheese_type_id"),
        nullable=False,
        index=True,
    )
    cheese_type: Mapped["CheeseType"] = relationship("CheeseType", back_populates="cheeses")
