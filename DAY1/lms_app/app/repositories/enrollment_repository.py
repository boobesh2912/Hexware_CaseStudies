from sqlalchemy.orm import Session
from app.models.enrollment_model import Enrollment
from app.schemas.enrollment_schema import EnrollmentCreate


class EnrollmentRepository:
    def __init__(self, db: Session):
        self.db = db

    def check_enrollment_exists(self, student_id: int, course_id: int) -> bool:
        return self.db.query(Enrollment).filter(
            Enrollment.student_id == student_id,
            Enrollment.course_id == course_id
        ).first() is not None

    def create_enrollment(self, enrollment: EnrollmentCreate) -> Enrollment:
        db_enrollment = Enrollment(
            student_id=enrollment.student_id,
            course_id=enrollment.course_id
        )
        self.db.add(db_enrollment)
        self.db.commit()
        self.db.refresh(db_enrollment)
        return db_enrollment

    def get_all_enrollments(self):
        return self.db.query(Enrollment).all()

    def get_enrollments_by_student(self, student_id: int):
        return self.db.query(Enrollment).filter(Enrollment.student_id == student_id).all()

    def get_enrollments_by_course(self, course_id: int):
        return self.db.query(Enrollment).filter(Enrollment.course_id == course_id).all()