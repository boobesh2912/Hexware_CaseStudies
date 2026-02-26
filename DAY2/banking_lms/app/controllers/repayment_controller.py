from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.services.repayment_service import RepaymentService
from app.schemas.repayment_schema import RepaymentCreate, RepaymentResponse

router = APIRouter(tags=["Repayments"])

# POST /repayments
@router.post("/repayments", response_model=RepaymentResponse, status_code=status.HTTP_201_CREATED)
def add_repayment(repayment_data: RepaymentCreate, db: Session = Depends(get_db)):
    return RepaymentService(db).add_repayment(repayment_data.model_dump())

# GET /loan-applications/{id}/repayments
@router.get("/loan-applications/{loan_application_id}/repayments", response_model=List[RepaymentResponse])
def get_repayments(loan_application_id: int, db: Session = Depends(get_db)):
    return RepaymentService(db).get_repayments_by_loan(loan_application_id)