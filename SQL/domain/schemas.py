from pydantic import BaseModel
from typing import Optional,List, Dict, Any

# class JobBase(BaseModel):
#     title: str
#     description: str | None = None

# class JobCreate(JobBase):
#     pass

# #reading with api models
# class Job(JobBase):
#     id: int
#     owner_id: int

#     class Config:
#         orm_mode = True

class JobBase(BaseModel):
    project: str
    hotspot_type: str
    max_temp: float
    string_tag: str
    priority: int
    
class JobCreate(JobBase):
    pass
    
class Job(JobBase):
    id: int

    class Config:
        orm_mode = True

class Properties(BaseModel):
    url: str
    var: str
    project: str
    Device: str
    Device_id: str
    IFOV: str
    MFOV: str
    ACC: str
    Date: str
    Time: str
    tag: str
    x: float
    y: float
    xmax: float
    ymax: float
    hotspot_type: str
    priority: int
    maxTemperature: float
    minTemperature: float
    maxIndex: List[int]
    minIndex: List[int]
    pv_brand: str
    normal_temp: float
    pv_min: str
    cell_size: str

class Geometry(BaseModel):
    type: str
    coordinates: List[str]

class Feature(BaseModel):
    type: str
    properties: Properties
    geometry: Geometry

class FeatureCollection(BaseModel):
    type: str
    features: List[Feature]

class AssignBase(BaseModel):
    job_id: int
    project: str
    hotspot_type: str
    max_temp: str
    string_tag: str
    priority: int
    header: str = ''
    worker: str = ''
    status: str = ''

class AssignCreate(AssignBase):
    pass

#reading with api models
class AssignResponse(AssignBase):
    class Config:
        orm_mode = True 
        

class HeadBase(BaseModel):
    name: str
    surname: str
    nickname: str
    department: str
    position: str
    tell: str
    email: str
    status: str
    
class HeadSent(BaseModel):
    name : str
    nickname: str
    id : int
    
class HeadCreate(HeadBase):
    pass

class HeadSent(BaseModel):
    name : str
    nickname: str
    id : int

class HeadRead(HeadBase):
    id: int

    class Config:
        orm_mode = True
        
class ManBase(BaseModel):
    name: str
    surname: str
    nickname: str
    header: Optional[str] = None
    department: str
    position: str
    tell: str
    email: str
    status: str
    head_id: int
        
class ManCreate(ManBase):
   pass

class ManResponse(ManBase):
    id: int
    class Config:
        orm_mode = True

class ManReadHead(ManBase):
    id: int
    head: Optional[HeadSent] 
     
    class Config:
        orm_mode = True
        
# class ManUpdate(BaseModel):
#     name: str
#     surname: str
#     nickname: str
#     header: str = None
#     department: str
#     position: str
#     tell: str
#     email: str
#     status: str

#     class Config:
#         orm_mode = True

class ManUpdate(BaseModel):
    name: str
    surname: str
    nickname: str
    department: str
    position: str
    tell: str
    email: str
    status: str
    head_id: int

    class Config:
        orm_mode = True

class ManReadHead2(ManUpdate):
    id: int
    header: str

    class Config:
        orm_mode = True

class HeadReadMan(HeadBase):
    id: int
    men: List[ManResponse] = [] 

    class Config:
        orm_mode = True
        
class TableName(BaseModel):
    name: str
    
##ManJobCreate
class ManjobCreate(BaseModel):
    job_id: Optional[int] = None
    project: str
    hotspot_type: str
    max_temp: str
    string_tag: str
    priority: int
    header: Optional[str] = None
    worker: Optional[str] = None
    status: Optional[str] = None
    note: Optional[str] = None

    class Config:
        orm_mode = True

class ManjobRead(ManjobCreate):
    id: int