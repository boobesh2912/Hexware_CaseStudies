from sqlalchemy import Column, Integer, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

class LoanStatus(str, enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"
    disbursed = "disbursed"
    closed = "closed"

class LoanApplication(Base):
    __tablename__ = "loan_applications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("loan_products.id"), nullable=False)
    requested_amount = Column(Float, nullable=False)
    approved_amount = Column(Float, nullable=True)       # nullable - only set when approved
    status = Column(Enum(LoanStatus), nullable=False, default=LoanStatus.pending)
    processed_by = Column(Integer, ForeignKey("users.id"), nullable=True)  # nullable - not yet processed

    # Many applications → One customer
    customer = relationship("User", foreign_keys=[user_id], back_populates="loan_applications")

    # Many applications → One loan product
    loan_product = relationship("LoanProduct", back_populates="loan_applications")

    # Many applications → One loan officer
    loan_officer = relationship("User", foreign_keys=[processed_by], back_populates="processed_applications")

    # One loan application → Many repayments
    repayments = relationship("Repayment", back_populates="loan_application")