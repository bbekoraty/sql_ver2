from sqlalchemy.orm import Session,joinedload
from sqlalchemy import text
from . import models, schemas
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



##Assign table
def get_assign(db: Session, assign_id: int):
    return db.query(models.Assign).filter(models.Assign.job_id == assign_id).first()

def get_assigns(db: Session, skip: int = 0):
    return db.query(models.Assign).offset(skip).all()

def create_assign(db: Session, assign: schemas.AssignCreate):
    db_assign = models.Assign(**assign.dict())
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

##db
def create_database(session: Session, db_name: str):
    try:
        session.connection().connection.set_isolation_level(0)  # set autocommit mode
        session.execute(text(f"CREATE DATABASE {db_name}"))
        session.connection().connection.set_isolation_level(1)  # reset isolation level
        return {"message": f"Database {db_name} created successfully."}
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        session.close()

def list_databases(session: Session):
    try:
        result = session.execute(text("SELECT datname FROM pg_database WHERE datistemplate = false"))
        databases = [row[0] for row in result]
        return {"databases": databases}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    
### Header 
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

def get_head_with_men(db: Session, head_id: int):
    return db.query(models.Head).filter(models.Head.id == head_id).options(joinedload(models.Head.men)).first()
