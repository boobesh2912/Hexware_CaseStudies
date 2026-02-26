from pydantic import BaseModel, Field
from app.models.loan_model import LoanStatus

class LoanCreate(BaseModel):
    applicant_name: str = Field(..., min_length=2, max_length=100)
    income: float = Field(..., gt=0, description="Monthly income")
    loan_amount: float = Field(..., gt=0, description="Requested loan amount")

class LoanResponse(BaseModel):
    id: int
    applicant_name: str
    income: float
    loan_amount: float
    status: LoanStatus

class LoanStatusUpdate(BaseModel):
    message: str
    status: LoanStatus
