from fastapi import FastAPI
from app.core.database import engine, Base

# Import all models so Base.metadata sees all tables
from app.models import user, loan_product, loan_application, repayment  # noqa

from app.middleware.cors import setup_cors
from app.middleware.logging_middleware import LoggingMiddleware

from app.exceptions.custom_exceptions import (
    UserNotFoundException, UserAlreadyExistsException,
    LoanProductNotFoundException, LoanApplicationNotFoundException,
    RepaymentNotFoundException, LoanAmountExceededException,
    UnauthorizedActionException, InvalidLoanStatusException
)
from app.exceptions.exception_handlers import (
    user_not_found_handler, user_already_exists_handler,
    loan_product_not_found_handler, loan_application_not_found_handler,
    repayment_not_found_handler, loan_amount_exceeded_handler,
    unauthorized_action_handler, invalid_loan_status_handler
)

from app.controllers import (
    user_controller, product_controller,
    application_controller, repayment_controller
)

app = FastAPI(title="Banking Loan Management System", version="1.0.0")

# Auto-create tables
Base.metadata.create_all(bind=engine)

# Middleware
setup_cors(app)
app.add_middleware(LoggingMiddleware)

# Exception handlers
app.add_exception_handler(UserNotFoundException, user_not_found_handler)
app.add_exception_handler(UserAlreadyExistsException, user_already_exists_handler)
app.add_exception_handler(LoanProductNotFoundException, loan_product_not_found_handler)
app.add_exception_handler(LoanApplicationNotFoundException, loan_application_not_found_handler)
app.add_exception_handler(RepaymentNotFoundException, repayment_not_found_handler)
app.add_exception_handler(LoanAmountExceededException, loan_amount_exceeded_handler)
app.add_exception_handler(UnauthorizedActionException, unauthorized_action_handler)
app.add_exception_handler(InvalidLoanStatusException, invalid_loan_status_handler)

# Routers
app.include_router(user_controller.router)
app.include_router(product_controller.router)
app.include_router(application_controller.router)
app.include_router(repayment_controller.router)

@app.get("/")
def root():
    return {"message": "Banking Loan Management System API is running"}