from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

class UserRole(str, enum.Enum):
    admin = "admin"
    loan_officer = "loan_officer"
    customer = "customer"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    role = Column(Enum(UserRole), nullable=False, default=UserRole.customer)
    hashed_password = Column(String, nullable=False)

    # Customer → Many loan applications
    loan_applications = relationship(
        "LoanApplication",
        foreign_keys="LoanApplication.user_id",
        back_populates="customer"
    )

    # Loan Officer → Many processed applications
    processed_applications = relationship(
        "LoanApplication",
        foreign_keys="LoanApplication.processed_by",
        back_populates="loan_officer"
    )