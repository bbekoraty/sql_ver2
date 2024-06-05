from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from domain import models
from domain import database
from domain.database import engine, Base
import domain.models as models


from routes import job,man,db,assign,head,table

# models.Base.metadata.create_all(bind=database.engine)
Base.metadata.create_all(bind=database.engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(job.router)
app.include_router(man.router)
app.include_router(head.router)
app.include_router(assign.router)
app.include_router(db.router)
app.include_router(table.router)
