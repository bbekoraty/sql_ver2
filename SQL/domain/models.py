from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, event
from sqlalchemy.orm import relationship
from .database import Base, SessionLocal

    
class Job(Base):
    __tablename__ = "maintenance"
    
    id = Column(Integer, primary_key=True, index=True)
    project = Column(String, nullable=False)
    hotspot_type = Column(String, nullable=False)
    max_temp = Column(String, nullable=False)
    string_tag = Column(String, nullable=False)
    priority = Column(Integer, nullable=False)
    
    assigns = relationship("Assign", back_populates="job")
    manjobs = relationship("Manjob",back_populates="maintenance")

class Head(Base):
    __tablename__ = "head"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    department = Column(String, nullable=False)
    position = Column(String, nullable=False)
    tell = Column(String, nullable=False)
    email = Column(String, nullable=False)
    status = Column(String, nullable=False)
    
    men = relationship("Man", back_populates="head")

class Man(Base):
    __tablename__ = "man"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    header = Column(String, nullable=True)
    department = Column(String, nullable=False)
    position = Column(String, nullable=False)
    tell = Column(String, nullable=False)
    email = Column(String, nullable=False)
    status = Column(String, nullable=False)
    head_id = Column(Integer, ForeignKey('head.id'), nullable=True)
    
    head = relationship("Head", back_populates="men")
    
# Event listener
@event.listens_for(Man, 'before_insert')
@event.listens_for(Man, 'before_update')
def update_header(mapper, connection, target):
    if target.head_id:
        session = SessionLocal()
        head = session.query(Head).filter(Head.id == target.head_id).first()
        target.header = head.name if head else None
        session.close()

class Assign(Base):
    __tablename__ = "assign"
    
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey('maintenance.id'), nullable=False)
    project = Column(String, nullable=False)
    hotspot_type = Column(String, nullable=False)
    max_temp = Column(String, nullable=False)
    string_tag = Column(String, nullable=False)
    priority = Column(Integer, nullable=False)
    header = Column(String)
    worker = Column(String)
    status = Column(String)
    
    job = relationship("Job", back_populates="assigns")
    
class Manjob(Base):
    __tablename__ = "manjob"
    
    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey('maintenance.id'), nullable=True)
    project = Column(String, nullable=False)
    hotspot_type = Column(String, nullable=False)
    max_temp = Column(String, nullable=False)
    string_tag = Column(String, nullable=False)
    priority = Column(Integer, nullable=False)
    header = Column(String, nullable=True)
    worker = Column(String, nullable=True)
    status = Column(String, nullable=True)
    note = Column(String, nullable=True)

    maintenance = relationship("Job", back_populates="manjobs")
    




