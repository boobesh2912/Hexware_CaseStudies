from sqlalchemy.orm import Session
from app.repositories.application_repository import ApplicationRepository
from app.repositories.product_repository import ProductRepository
from app.repositories.user_repository import UserRepository
from app.exceptions.custom_exceptions import (
    LoanApplicationNotFoundException,
    LoanProductNotFoundException,
    UserNotFoundException,
    LoanAmountExceededException,
    UnauthorizedActionException,
    InvalidLoanStatusException
)
from app.models.loan_application import LoanStatus
from app.models.user import UserRole

class ApplicationService:
    def __init__(self, db: Session):
        self.app_repo = ApplicationRepository(db)
        self.product_repo = ProductRepository(db)
        self.user_repo = UserRepository(db)

    def create_application(self, application_data: dict):
        # Validate user exists
        user = self.user_repo.get_user_by_id(application_data["user_id"])
        if not user:
            raise UserNotFoundException(application_data["user_id"])

        # Validate product exists
        product = self.product_repo.get_product_by_id(application_data["product_id"])
        if not product:
            raise LoanProductNotFoundException(application_data["product_id"])

        # Business rule: requested_amount cannot exceed product max_amount
        if application_data["requested_amount"] > product.max_amount:
            raise LoanAmountExceededException(application_data["requested_amount"], product.max_amount)

        return self.app_repo.create_application(application_data)

    def get_application(self, application_id: int):
        app = self.app_repo.get_application_by_id(application_id)
        if not app:
            raise LoanApplicationNotFoundException(application_id)
        return app

    def get_all_applications(self, skip: int = 0, limit: int = 10):
        return self.app_repo.get_all_applications(skip, limit)

    def update_status(self, application_id: int, update_data: dict):
        application = self.get_application(application_id)

        # Business rule: only loan_officer can approve/reject
        officer = self.user_repo.get_user_by_id(update_data["processed_by"])
        if not officer:
            raise UserNotFoundException(update_data["processed_by"])
        if officer.role != UserRole.loan_officer:
            raise UnauthorizedActionException("Only loan officers can approve or reject applications")

        new_status = update_data["status"]

        # Business rule: cannot disburse unless status is approved
        if new_status == LoanStatus.disbursed and application.status != LoanStatus.approved:
            raise InvalidLoanStatusException("Loan can only be disbursed if it is approved first")

        # Business rule: cannot approve if already rejected or closed
        if application.status in [LoanStatus.rejected, LoanStatus.closed]:
            raise InvalidLoanStatusException(f"Cannot update a {application.status} loan application")

        return self.app_repo.update_status(application, update_data)