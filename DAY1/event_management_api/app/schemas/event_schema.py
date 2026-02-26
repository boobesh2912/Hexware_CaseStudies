from pydantic import BaseModel, Field
from typing import Optional

class EventBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    location: str
    capacity: int = Field(..., gt=0) 

class EventCreate(EventBase):
    pass

class EventResponse(EventBase):
    id: int

    class Config:
        from_attributes = True