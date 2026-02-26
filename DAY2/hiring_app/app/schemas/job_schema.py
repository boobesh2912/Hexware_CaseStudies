from pydantic import BaseModel, Field
from typing import Optional

class JobBase(BaseModel):
    title: str = Field(..., min_length=2, max_length=200)
    description: Optional[str] = None
    salary: Optional[float] = Field(None, gt=0)
    company_id: int

class JobCreate(JobBase):
    pass

# JobUpdate allows partial updates — all fields optional
class JobUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    salary: Optional[float] = None
    company_id: Optional[int] = None

class JobResponse(JobBase):
    id: int

    class Config:
        from_attributes = True