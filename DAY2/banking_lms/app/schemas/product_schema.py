from pydantic import BaseModel, Field
from typing import Optional

class LoanProductCreate(BaseModel):
    product_name: str = Field(..., min_length=2)
    interest_rate: float = Field(..., gt=0)
    max_amount: float = Field(..., gt=0)
    tenure_months: int = Field(..., gt=0)
    description: Optional[str] = None

class LoanProductUpdate(BaseModel):
    product_name: Optional[str] = None
    interest_rate: Optional[float] = None
    max_amount: Optional[float] = None
    tenure_months: Optional[int] = None
    description: Optional[str] = None

class LoanProductResponse(LoanProductCreate):
    id: int

    class Config:
        from_attributes = True