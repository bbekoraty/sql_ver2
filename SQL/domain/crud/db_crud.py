from sqlalchemy.orm import Session,joinedload
from sqlalchemy import text
from . import models, schemas
from fastapi import HTTPException


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
    