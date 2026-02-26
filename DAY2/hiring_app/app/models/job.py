from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.core.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    salary = Column(Float, nullable=True)
    company_id = Column(Integer, nullable=False)

    # One Job → Many Applications
    applications = relationship("Application", back_populates="job")