from sqlalchemy import Table, Column, Integer, String, ForeignKey
from ..database import metadata, engine
from ..models import Base

def create_dynamic_table(table_name: str):
    return Table(
        table_name,
        metadata,
        Column('id', Integer, primary_key=True, index=True),
        Column('job_id', Integer, nullable=True),
        Column('project', String, nullable=False),
        Column('hotspot_type', String, nullable=False),
        Column('max_temp', String, nullable=False),
        Column('string_tag', String, nullable=False),
        Column('priority', Integer, nullable=False),
        Column('header', String, nullable=True),
        Column('worker', String, nullable=True),
        Column('status', String, nullable=True),
        Column('note', String, nullable=True),
    )

