from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class CheeseTypeBase(BaseModel):
    name: str
    description: Optional[str]

    class Config:
        from_attributes = True


class CheeseTypeCreate(CheeseTypeBase):
    pass


class CheeseTypeUpdate(CheeseTypeBase):
    id: int


class CheeseTypeRead(CheeseTypeUpdate):
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
