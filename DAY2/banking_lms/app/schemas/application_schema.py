from pydantic import BaseModel, Field
from typing import Optional
from app.models.loan_application import LoanStatus

class LoanApplicationCreate(BaseModel):
    user_id: int
    product_id: int
    requested_amount: float = Field(..., gt=0)

class LoanApplicationStatusUpdate(BaseModel):
    status: LoanStatus
    approved_amount: Optional[float] = None
    processed_by: int  # loan officer id

class LoanApplicationResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    requested_amount: float
    approved_amount: Optional[float] = None
    status: LoanStatus
    processed_by: Optional[int] = None

    class Config:
        from_attributes = True