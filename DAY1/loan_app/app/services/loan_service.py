from fastapi import HTTPException, status
from app.repositories.loan_repository import LoanRepository
from app.models.loan_model import LoanApplication, LoanStatus
from app.schemas.loan_schema import LoanCreate
from typing import List

ELIGIBILITY_MULTIPLIER = 10

class LoanService:
    def __init__(self, repository: LoanRepository):
        self.repository = repository

    def submit_application(self, data: LoanCreate) -> LoanApplication:
        eligibility_limit = data.income * ELIGIBILITY_MULTIPLIER
        if data.loan_amount > eligibility_limit:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Loan amount exceeds eligibility limit. Max eligible: {eligibility_limit}"
            )
        return self.repository.create_loan(
            applicant_name=data.applicant_name,
            income=data.income,
            loan_amount=data.loan_amount
        )

    def get_application(self, loan_id: int) -> LoanApplication:
        loan = self.repository.get_loan_by_id(loan_id)
        if not loan:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Loan application not found"
            )
        return loan

    def get_all_applications(self) -> List[LoanApplication]:
        return self.repository.get_all_loans()

    def approve_loan(self, loan_id: int) -> LoanApplication:
        loan = self.get_application(loan_id)
        if loan.status != LoanStatus.PENDING:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Only pending loans can be approved"
            )
        return self.repository.update_status(loan_id, LoanStatus.APPROVED)

    def reject_loan(self, loan_id: int) -> LoanApplication:
        loan = self.get_application(loan_id)
        if loan.status != LoanStatus.PENDING:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Only pending loans can be rejected"
            )
        return self.repository.update_status(loan_id, LoanStatus.REJECTED)
