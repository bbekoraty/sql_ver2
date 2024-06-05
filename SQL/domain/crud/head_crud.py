from sqlalchemy.orm import Session,joinedload
from sqlalchemy import text
from . import models, schemas
from fastapi import HTTPException


def get_heads(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Head).offset(skip).limit(limit).all()

def create_head(db: Session, head: schemas.HeadCreate):
    db_head = models.Head(
        name=head.name,
        surname=head.surname,
        nickname=head.nickname,
        department=head.department,
        position=head.position,
        tell=head.tell,
        email=head.email,
        status=head.status
    )
    db.add(db_head)
    db.commit()
    db.refresh(db_head)
    return db_head

def get_head_with_men(db: Session, head_id: int):
    return db.query(models.Head).filter(models.Head.id == head_id).options(joinedload(models.Head.men)).first()
