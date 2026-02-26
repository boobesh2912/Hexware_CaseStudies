from fastapi import APIRouter, Depends, status
from typing import List
from app.schemas.loan_schema import LoanCreate, LoanResponse, LoanStatusUpdate
from app.services.loan_service import LoanService
from app.dependencies.loan_dependency import get_loan_service

router = APIRouter(prefix="/loans", tags=["Loans"])

@router.post("", response_model=LoanResponse, status_code=status.HTTP_201_CREATED)
def submit_loan(data: LoanCreate, service: LoanService = Depends(get_loan_service)):
    loan = service.submit_application(data)
    return loan.__dict__

@router.get("", response_model=List[LoanResponse], status_code=status.HTTP_200_OK)
def get_all_loans(service: LoanService = Depends(get_loan_service)):
    return [l.__dict__ for l in service.get_all_applications()]

@router.get("/{loan_id}", response_model=LoanResponse, status_code=status.HTTP_200_OK)
def get_loan(loan_id: int, service: LoanService = Depends(get_loan_service)):
    loan = service.get_application(loan_id)
    return loan.__dict__

@router.put("/{loan_id}/approve", response_model=LoanStatusUpdate, status_code=status.HTTP_200_OK)
def approve_loan(loan_id: int, service: LoanService = Depends(get_loan_service)):
    loan = service.approve_loan(loan_id)
    return {"message": "Loan approved successfully", "status": loan.status}

@router.put("/{loan_id}/reject", response_model=LoanStatusUpdate, status_code=status.HTTP_200_OK)
def reject_loan(loan_id: int, service: LoanService = Depends(get_loan_service)):
    loan = service.reject_loan(loan_id)
    return {"message": "Loan rejected", "status": loan.status}
