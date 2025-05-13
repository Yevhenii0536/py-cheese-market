from sqlalchemy.orm import Session
from schemas.cheese.type import CheeseTypeCreate
from db.models.cheese import CheeseType


def read_cheese_types_db(db: Session):
    return db.query(CheeseType).all()


def create_cheese_type_db(db: Session, cheese_type: CheeseTypeCreate):
    cheese_type_db = CheeseType(
        name=cheese_type.name,
        description=cheese_type.description
    )

    db.add(cheese_type_db)
    db.commit()
    db.refresh(cheese_type_db)

    return cheese_type_db
