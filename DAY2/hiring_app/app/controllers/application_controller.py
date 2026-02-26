from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.services.application_service import ApplicationService
from app.schemas.application_schema import ApplicationCreate, ApplicationResponse

router = APIRouter(tags=["Applications"])

# POST /applications - Apply for a job
@router.post("/applications", response_model=ApplicationResponse, status_code=status.HTTP_201_CREATED)
def apply_for_job(application_data: ApplicationCreate, db: Session = Depends(get_db)):
    service = ApplicationService(db)
    return service.apply_for_job(application_data.model_dump())

# GET /applications/{id} - View a specific application
@router.get("/applications/{application_id}", response_model=ApplicationResponse, status_code=status.HTTP_200_OK)
def get_application(application_id: int, db: Session = Depends(get_db)):
    service = ApplicationService(db)
    return service.get_application(application_id)

# GET /users/{user_id}/applications - Nested query: all applications for a user
# This is the nested route pattern from the PDF
@router.get("/users/{user_id}/applications", response_model=List[ApplicationResponse], status_code=status.HTTP_200_OK)
def get_user_applications(user_id: int, db: Session = Depends(get_db)):
    service = ApplicationService(db)
    return service.get_user_applications(user_id)