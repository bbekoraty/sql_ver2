from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from domain import crud , database, schemas
from domain import man_crud

router = APIRouter(
    prefix="/man",
    tags=["man"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.ManResponse)
def create_man(man: schemas.ManCreate, db: Session = Depends(database.get_db)):
    return man_crud.create_man(db=db, man=man)

@router.get("/", response_model=List[schemas.ManResponse])
def get_mens(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    men = man_crud.get_lsman(db=db, skip=skip, limit=limit)
    return men

@router.get("/{man_id}", response_model=schemas.ManResponse)
def get_man(man_id: int, db: Session = Depends(database.get_db)):
    db_man = man_crud.get_man(db=db, man_id=man_id)
    if db_man is None:
        raise HTTPException(status_code=404, detail="Man not found")
    return db_man

@router.get("/men_with_heads/", response_model=List[schemas.ManReadHead])
def read_men_with_heads(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return man_crud.get_men_with_heads(db=db, skip=skip, limit=limit)

# @router.put("/update/{man_id}", response_model=schemas.ManReadHead)
# def update_assign(man_id: int, man: schemas.ManReadHead, db: Session = Depends(database.get_db)):
#     db_assign = man_crud.update_man(db, man_id=man_id, man=man)
#     if db_assign is None:
#         raise HTTPException(status_code=404, detail="Assign not found")
#     return db_assign

@router.put("/update/{man_id}", response_model=schemas.ManReadHead)
def update_man(man_id: int, man: schemas.ManUpdate, db: Session = Depends(database.get_db)):
    db_man = man_crud.update_man(db, man_id, man)
    if db_man is None:
        raise HTTPException(status_code=404, detail="Man not found")
    return db_man
