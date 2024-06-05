from sqlalchemy.orm import Session,joinedload
from sqlalchemy import text
from .. import models, schemas
from fastapi import HTTPException


##Assign table
def get_assign(db: Session, assign_id: int):
    return db.query(models.Assign).filter(models.Assign.job_id == assign_id).first()

def get_assigns(db: Session, skip: int = 0):
    return db.query(models.Assign).offset(skip).all()

# def create_assign(db: Session, assign: schemas.AssignCreate):
#     db_assign = models.Assign(**assign.dict())
#     db.add(db_assign)
#     db.commit()
#     db.refresh(db_assign)
#     return db_assign

def create_assign(db: Session, assign: schemas.AssignCreate):
    db_assign = models.Assign(
        job_id=assign.job_id,
        project=assign.project,
        hotspot_type=assign.hotspot_type,
        max_temp=assign.max_temp,
        string_tag=assign.string_tag,
        priority=assign.priority,
        header=assign.header,
        worker=assign.worker,
        status=assign.status
    )
    db.add(db_assign)
    db.commit()
    db.refresh(db_assign)
    return db_assign

def delete_assign(db: Session, assign_id: int):
    db_assign = db.query(models.Assign).filter(models.Assign.id == assign_id).first()
    if db_assign:
        db.delete(db_assign)
        db.commit()
    return db_assign

def update_assign(db: Session, assign_id: int, assign: schemas.AssignCreate):
    db_assign = db.query(models.Assign).filter(models.Assign.id == assign_id).first()
    if db_assign:
        for key, value in assign.dict().items():
            setattr(db_assign, key, value)
        db.commit()
        db.refresh(db_assign)
    return db_assign