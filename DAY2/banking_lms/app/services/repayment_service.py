from sqlalchemy.orm import Session
from datetime import date
from app.repositories.repayment_repository import RepaymentRepository
from app.repositories.application_repository import ApplicationRepository
from app.exceptions.custom_exceptions import (
    LoanApplicationNotFoundException,
    InvalidLoanStatusException
)
from app.models.loan_application import LoanStatus

class RepaymentService:
    def __init__(self, db: Session):
        self.repayment_repo = RepaymentRepository(db)
        self.app_repo = ApplicationRepository(db)

    def add_repayment(self, repayment_data: dict):
        loan_id = repayment_data["loan_application_id"]

        # Validate loan exists
        application = self.app_repo.get_application_by_id(loan_id)
        if not application:
            raise LoanApplicationNotFoundException(loan_id)

        # Business rule: can only repay disbursed loans
        if application.status != LoanStatus.disbursed:
            raise InvalidLoanStatusException("Repayments can only be made on disbursed loans")

        # Set payment date if not provided
        if not repayment_data.get("payment_date"):
            repayment_data["payment_date"] = date.today()

        repayment = self.repayment_repo.create_repayment(repayment_data)

        # Business rule: close loan after full repayment
        total_paid = self.repayment_repo.get_total_paid(loan_id)
        approved_amount = application.approved_amount or application.requested_amount
        if total_paid >= approved_amount:
            self.app_repo.update_status(application, {"status": LoanStatus.closed})

        return repayment

    def get_repayments_by_loan(self, loan_application_id: int):
        application = self.app_repo.get_application_by_id(loan_application_id)
        if not application:
            raise LoanApplicationNotFoundException(loan_application_id)
        return self.repayment_repo.get_repayments_by_loan(loan_application_id)