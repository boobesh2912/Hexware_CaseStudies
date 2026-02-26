from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from app.models.repayment import PaymentStatus

class RepaymentCreate(BaseModel):
    loan_application_id: int
    amount_paid: float = Field(..., gt=0)
    payment_date: Optional[date] = None

class RepaymentResponse(BaseModel):
    id: int
    loan_application_id: int
    amount_paid: float
    payment_date: date
    payment_status: PaymentStatus

    class Config:
        from_attributes = True