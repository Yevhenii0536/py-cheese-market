from sqlalchemy.orm import Session, joinedload

from schemas.cheese.type import CheeseTypeCreate
from schemas.cheese.cheese import CheeseCreate

from db.models.cheese import CheeseType, Cheese

from fastapi import HTTPException, status

from validators.cheese import (
    check_name_duplicate_on_create,
    check_name_duplicate_on_update,
)


def create_cheese_db(db: Session, cheese: CheeseCreate):
    cheese_db = Cheese(**cheese.model_dump())

    db.add(cheese_db)
    db.commit()
    db.refresh(cheese_db)

    db.refresh(cheese_db, attribute_names=["cheese_type"])

    return cheese_db


def read_cheese_db(db: Session):
    # return db.query(Cheese).all()
    return db.query(Cheese).options(joinedload(Cheese.cheese_type)).all()


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
