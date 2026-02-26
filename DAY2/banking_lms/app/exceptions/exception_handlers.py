from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions.custom_exceptions import (
    UserNotFoundException, UserAlreadyExistsException,
    LoanProductNotFoundException, LoanApplicationNotFoundException,
    RepaymentNotFoundException, LoanAmountExceededException,
    UnauthorizedActionException, InvalidLoanStatusException
)

async def user_not_found_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(status_code=404, content={"detail": str(exc)})

async def user_already_exists_handler(request: Request, exc: UserAlreadyExistsException):
    return JSONResponse(status_code=400, content={"detail": str(exc)})

async def loan_product_not_found_handler(request: Request, exc: LoanProductNotFoundException):
    return JSONResponse(status_code=404, content={"detail": str(exc)})

async def loan_application_not_found_handler(request: Request, exc: LoanApplicationNotFoundException):
    return JSONResponse(status_code=404, content={"detail": str(exc)})

async def repayment_not_found_handler(request: Request, exc: RepaymentNotFoundException):
    return JSONResponse(status_code=404, content={"detail": str(exc)})

async def loan_amount_exceeded_handler(request: Request, exc: LoanAmountExceededException):
    return JSONResponse(status_code=400, content={"detail": str(exc)})

async def unauthorized_action_handler(request: Request, exc: UnauthorizedActionException):
    return JSONResponse(status_code=403, content={"detail": str(exc)})

async def invalid_loan_status_handler(request: Request, exc: InvalidLoanStatusException):
    return JSONResponse(status_code=400, content={"detail": str(exc)})