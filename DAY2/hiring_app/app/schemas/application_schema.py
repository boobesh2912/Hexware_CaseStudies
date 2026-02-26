from pydantic import BaseModel
from app.models.application import ApplicationStatus

class ApplicationCreate(BaseModel):
    user_id: int
    job_id: int

class ApplicationResponse(BaseModel):
    id: int
    user_id: int
    job_id: int
    status: ApplicationStatus

    class Config:
        from_attributes = True