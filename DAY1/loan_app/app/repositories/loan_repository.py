from typing import List, Optional
from app.models.loan_model import LoanApplication, LoanStatus

class LoanRepository:
    def __init__(self):
        self._loans: List[LoanApplication] = []
        self._counter: int = 1

    def create_loan(self, applicant_name: str, income: float, loan_amount: float) -> LoanApplication:
        loan = LoanApplication(
            id=self._counter,
            applicant_name=applicant_name,
            income=income,
            loan_amount=loan_amount
        )
        self._loans.append(loan)
        self._counter += 1
        return loan

    def get_loan_by_id(self, loan_id: int) -> Optional[LoanApplication]:
        for loan in self._loans:
            if loan.id == loan_id:
                return loan
        return None

    def get_all_loans(self) -> List[LoanApplication]:
        return self._loans

    def update_status(self, loan_id: int, status: LoanStatus) -> Optional[LoanApplication]:
        for loan in self._loans:
            if loan.id == loan_id:
                loan.status = status
                return loan
        return None
