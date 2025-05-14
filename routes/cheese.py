from crud.cheese.create import (
    create_cheese_type_db as types_create,
    read_cheese_types_db as types_read,
    update_cheese_type_db as types_update,
    delete_cheese_type_db as types_delete,
)

from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from db.engine import get_db

from schemas.cheese.type import CheeseTypeCreate, CheeseTypeRead, CheeseTypeUpdate

from typing import List


router = APIRouter()

TYPES_PATH = "/cheese_types"
CHEESE_PATH = "/cheese"


@router.post(TYPES_PATH, response_model=CheeseTypeRead)
def create_cheese_type(cheese_type: CheeseTypeCreate, db: Session = Depends(get_db)):
    return types_create(db=db, cheese_type=cheese_type)


@router.get(TYPES_PATH, response_model=List[CheeseTypeRead])
def get_cheese_types(db: Session = Depends(get_db)):
    return types_read(db=db)


@router.patch(TYPES_PATH, response_model=CheeseTypeRead)
def update_cheese_type(cheese_type: CheeseTypeUpdate, db: Session = Depends(get_db)):
    return types_update(cheese_type=cheese_type, db=db)


@router.delete(TYPES_PATH, response_model=CheeseTypeRead)
def delete_cheese_type(cheese_type_id: int, db: Session = Depends(get_db)):
    return types_delete(cheese_type_id=cheese_type_id, db=db)
