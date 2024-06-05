from sqlalchemy.orm import Session,joinedload
from sqlalchemy import text
from .. import models, schemas
from fastapi import HTTPException

##MAN SECTION##
# def create_man(db: Session, man: schemas.ManCreate):
#     db_man = models.Man(**man.dict())
#     db.add(db_man)
#     db.commit()
#     db.refresh(db_man)
#     return db_man

def get_man(db: Session, man_id: int):
    return db.query(models.Man).filter(models.Man.id == man_id).first()

def get_lsman(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Man).offset(skip).limit(limit).all()

def get_man_head(db: Session, man_id: int):
    return db.query(models.Man).filter(models.Man.id == man_id).first()


def create_man(db: Session, man: schemas.ManCreate):
    db_man = models.Man(
        name=man.name,
        surname=man.surname,
        nickname=man.nickname,
        header=man.header,
        department=man.department,
        position=man.position,
        tell=man.tell,
        email=man.email,
        status=man.status,
        head_id=man.head_id
    )
    db.add(db_man)
    db.commit()
    db.refresh(db_man)
    return db_man

def get_men_with_heads(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Man).options(joinedload(models.Man.head)).offset(skip).limit(limit).all()

def update_man(db: Session, man_id: int, man: schemas.ManUpdate):
    db_man = db.query(models.Man).filter(models.Man.id == man_id).first()
    if db_man:
        for key, value in man.dict().items():
            setattr(db_man, key, value)
        db.commit()
        db.refresh(db_man)
    return db_man
