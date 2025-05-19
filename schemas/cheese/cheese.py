from pydantic import BaseModel
from db.models.cheese import PackagingType
from schemas.cheese.type import CheeseTypeRead
from typing import Optional
from datetime import datetime


class CheeseBase(BaseModel):
    title: str
    price: float
    packaging_type: PackagingType

    class Config:
        from_attributes = True


class CheeseRead(CheeseBase):
    id: int
    cheese_type: Optional[CheeseTypeRead]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class CheeseCreate(CheeseBase):
    cheese_type_id: int
