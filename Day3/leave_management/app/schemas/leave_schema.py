from pydantic import BaseModel
from datetime import date
from typing import Optional

class LeaveBase(BaseModel):
    start_date: date
    end_date: date
    reason: str

class LeaveCreate(LeaveBase):
    pass

class LeaveUpdate(BaseModel):
    status: str # APPROVED or REJECTED

class LeaveResponse(LeaveBase):
    id: int
    employee_id: int
    status: str
    approved_by: Optional[int]

    class Config:
        from_attributes = True