from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from domain import assign_crud
from .. import crud, schemas, database

router = APIRouter(
    prefix="/manjob",
    tags=["manjob"],
    responses={404: {"description": "Not found"}},
)

# @router.post("/", response_model=schemas.ManjobRead)
# def create_manjob(manjob: schemas.ManjobCreate, db: Session = Depends(database.get_db)):
#     return crud.create_manjob(db=db, manjob=manjob)

# @router.get("/", response_model=List[schemas.ManjobRead])
# def read_manjobs(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
#     return db.query(models.Manjob).offset(skip).limit(limit).all()
