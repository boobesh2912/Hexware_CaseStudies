from pydantic import BaseModel
from typing import Optional

class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    manager_id: Optional[int] = None

class DepartmentResponse(DepartmentBase):
    id: int
    manager_id: Optional[int]

    class Config:
        from_attributes = True