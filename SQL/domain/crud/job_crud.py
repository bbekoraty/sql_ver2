from sqlalchemy.orm import Session,joinedload
from sqlalchemy import text
from .. import models, schemas
from fastapi import HTTPException



##JOB SECTION##
def create_Job(db: Session, list: schemas.JobCreate):
    db_list = models.Job(
        project=list.project,
        hotspot_type=list.hotspot_type,
        max_temp=list.max_temp,
        string_tag=list.string_tag,
        priority = list.priority
    )
    db.add(db_list)
    db.commit()
    db.refresh(db_list)
    return db_list

def get_Jobs(db: Session, skip: int = 0):
    return db.query(models.Job).offset(skip).all()

def get_Job(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()
