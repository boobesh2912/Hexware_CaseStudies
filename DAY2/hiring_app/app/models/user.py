from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

# Python enum defines the allowed role values
class UserRole(str, enum.Enum):
    admin = "admin"
    recruiter = "recruiter"
    candidate = "candidate"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)   # unique=True enforces no duplicate emails
    role = Column(Enum(UserRole), nullable=False, default=UserRole.candidate)
    hashed_password = Column(String, nullable=False)

    # One User → Many Applications
    # back_populates links both sides of the relationship
    applications = relationship("Application", back_populates="user")