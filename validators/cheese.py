from sqlalchemy.orm import Session
from db.models.cheese import CheeseType
from fastapi import HTTPException, status


def check_name_duplicate_on_create(db: Session, cheese_type: CheeseType):
    name = cheese_type.name

    if db.query(CheeseType).filter(CheeseType.name == cheese_type.name).first():
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Cheese type '{name}' already exists"
        )


def check_name_duplicate_on_update(db: Session, cheese_type_id: int, new_name: str):
    existing = (
        db.query(CheeseType)
        .filter(CheeseType.name == new_name, CheeseType.id != cheese_type_id)
        .first()
    )
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Another cheese type with name '{new_name}' already exists"
        )
    