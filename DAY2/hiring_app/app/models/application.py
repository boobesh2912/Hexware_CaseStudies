from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

class ApplicationStatus(str, enum.Enum):
    applied = "applied"
    shortlisted = "shortlisted"
    rejected = "rejected"

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)   # FK → users table
    job_id = Column(Integer, ForeignKey("jobs.id"), nullable=False)     # FK → jobs table
    status = Column(Enum(ApplicationStatus), nullable=False, default=ApplicationStatus.applied)

    # Many Applications → One User
    user = relationship("User", back_populates="applications")

    # Many Applications → One Job
    job = relationship("Job", back_populates="applications")