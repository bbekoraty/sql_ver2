from sqlalchemy.orm import Session
from . import models, schemas

def create_manjob(db: Session, manjob: schemas.ManjobCreate):
    db_manjob = models.Manjob(**manjob.dict())
    db.add(db_manjob)
    db.commit()
    db.refresh(db_manjob)
    return db_manjob
