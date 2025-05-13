from pydantic import BaseModel
from db.models.cheese import CheeseType, PackagingType


class CheeseBase(BaseModel):
    id: int
    title: str
    price: float
    packaging_type: PackagingType
    cheese_type: CheeseType

    class Config:
        orm_mode = True