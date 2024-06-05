from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from domain import table_crud ,schemas ,database

router = APIRouter(
    prefix="/table",
    tags=["table"],
    responses={404: {"description": "Not found"}},
)

@router.post("/create_table/")
def create_table(table_name: schemas.TableName, db: Session = Depends(database.get_db)):
    table = table_crud.create_dynamic_table(table_name.name)
    database.metadata.create_all(bind=database.engine, tables=[table])
    return {"message": f"Table {table_name.name} created successfully."}

@router.get("/tables/")
def get_tables():
    return list(database.metadata.tables.keys())