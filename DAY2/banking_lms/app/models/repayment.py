from sqlalchemy import Column, Integer, Float, ForeignKey, Enum, Date
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum
from datetime import date

class PaymentStatus(str, enum.Enum):
    completed = "completed"
    pending = "pending"

class Repayment(Base):
    __tablename__ = "repayments"

    id = Column(Integer, primary_key=True, index=True)
    loan_application_id = Column(Integer, ForeignKey("loan_applications.id"), nullable=False)
    amount_paid = Column(Float, nullable=False)
    payment_date = Column(Date, nullable=False, default=date.today)
    payment_status = Column(Enum(PaymentStatus), nullable=False, default=PaymentStatus.completed)

    # Many repayments → One loan application
    loan_application = relationship("LoanApplication", back_populates="repayments")