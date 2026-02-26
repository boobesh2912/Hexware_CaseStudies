from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.db import Base


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    duration = Column(Integer, nullable=False)

    enrollments = relationship("Enrollment", back_populates="course")