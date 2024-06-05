from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from domain import schemas, crud, database, geo_sort
from typing import List
from domain import head_crud

router = APIRouter(
    prefix="/head",
    tags=["head"],
    responses={404: {"description": "Not found"}},
)

@router.post("/create/", response_model=schemas.HeadRead)
def create_head(head: schemas.HeadCreate, db: Session = Depends(database.get_db)):
    return head_crud.create_head(db=db, head=head)

@router.get("/get/", response_model=List[schemas.HeadRead])
def read_heads(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return head_crud.get_heads(db=db, skip=skip, limit=limit)


@router.get("/head_with_men/{head_id}", response_model=schemas.HeadReadMan)
def read_head_with_men(head_id: int, db: Session = Depends(database.get_db)):
    head = head_crud.get_head_with_men(db=db, head_id=head_id)
    if head is None:
        raise HTTPException(status_code=404, detail="Head not found")
    return head