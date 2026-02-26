from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.services.application_service import ApplicationService
from app.schemas.application_schema import (
    LoanApplicationCreate,
    LoanApplicationStatusUpdate,
    LoanApplicationResponse
)

router = APIRouter(prefix="/loan-applications", tags=["Loan Applications"])

@router.post("/", response_model=LoanApplicationResponse, status_code=status.HTTP_201_CREATED)
def create_application(application_data: LoanApplicationCreate, db: Session = Depends(get_db)):
    return ApplicationService(db).create_application(application_data.model_dump())

@router.get("/", response_model=List[LoanApplicationResponse])
def get_applications(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return ApplicationService(db).get_all_applications(skip, limit)

@router.get("/{application_id}", response_model=LoanApplicationResponse)
def get_application(application_id: int, db: Session = Depends(get_db)):
    return ApplicationService(db).get_application(application_id)

@router.put("/{application_id}/status", response_model=LoanApplicationResponse)
def update_status(application_id: int, update_data: LoanApplicationStatusUpdate, db: Session = Depends(get_db)):
    return ApplicationService(db).update_status(application_id, update_data.model_dump())