from sqlalchemy.orm import Session
from schemas.cheese.type import CheeseTypeCreate
from db.models.cheese import CheeseType
from fastapi import HTTPException, status
from validators.cheese import (
    check_name_duplicate_on_create,
    check_name_duplicate_on_update,
)


def create_cheese_type_db(db: Session, cheese_type: CheeseTypeCreate):
    check_name_duplicate_on_create(db=db, cheese_type=cheese_type)

    cheese_type_db = CheeseType(
        name=cheese_type.name,
        description=cheese_type.description
    )

    db.add(cheese_type_db)
    db.commit()
    db.refresh(cheese_type_db)

    return cheese_type_db


def read_cheese_types_db(db: Session):
    return db.query(CheeseType).all()


def update_cheese_type_db(cheese_type: CheeseType, db: Session):
    cheese_type_db = db.query(CheeseType).filter(CheeseType.id == cheese_type.id).first()

    if cheese_type_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cheese type not found")
    
    check_name_duplicate_on_update(db, cheese_type.id, cheese_type.name)

    for key, value in vars(cheese_type).items():
        if key in ['id', 'created_at']:
            continue

        setattr(cheese_type_db, key, value)

    db.commit()

    return cheese_type_db


def delete_cheese_type_db(db: Session, cheese_type_id: int):
    cheese_type_db = db.query(CheeseType).filter(CheeseType.id == cheese_type_id).first()

    if cheese_type_db is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cheese type not found")
    

    db.delete(cheese_type_db)
    db.commit()

    return cheese_type_db
