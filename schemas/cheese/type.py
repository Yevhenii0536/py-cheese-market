from pydantic import BaseModel
from typing import Optional


class CheeseTypeBase(BaseModel):
    name: str
    description: Optional[str]

    class Config:
        from_attributes = True


class CheeseTypeCreate(CheeseTypeBase):
    pass


class CheeseType(CheeseTypeBase):
    id: int