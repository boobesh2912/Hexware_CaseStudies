from enum import Enum

class LoanStatus(str, Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"

class LoanApplication:
    def __init__(self, id: int, applicant_name: str, income: float, loan_amount: float):
        self.id = id
        self.applicant_name = applicant_name
        self.income = income
        self.loan_amount = loan_amount
        self.status = LoanStatus.PENDING
