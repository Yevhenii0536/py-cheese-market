from crud.cheese.create import read_cheese_types_db

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from db.engine import get_db

from schemas.cheese.type import CheeseType

from typing import List


router = APIRouter()


@router.get("/cheese_types", response_model=List[CheeseType])
def get_cheese_types(db: Session = Depends(get_db)):
    return read_cheese_types_db(db=db)