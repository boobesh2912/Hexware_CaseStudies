from app.repositories.loan_repository import LoanRepository
from app.services.loan_service import LoanService

# Singleton-style in-memory repository
_repository = LoanRepository()

def get_loan_service() -> LoanService:
    return LoanService(_repository)
