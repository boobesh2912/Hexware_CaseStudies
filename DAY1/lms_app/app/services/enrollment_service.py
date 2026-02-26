from fastapi import HTTPException, status
from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.student_repository import StudentRepository
from app.repositories.course_repository import CourseRepository
from app.schemas.enrollment_schema import EnrollmentCreate


class EnrollmentService:
    def __init__(self, enrollment_repository: EnrollmentRepository,
                 student_repository: StudentRepository,
                 course_repository: CourseRepository):
        self.enrollment_repository = enrollment_repository
        self.student_repository = student_repository
        self.course_repository = course_repository

    def enroll_student(self, enrollment: EnrollmentCreate):
        # check if student exists
        student = self.student_repository.get_student_by_id(enrollment.student_id)
        if not student:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

        # check if course exists
        course = self.course_repository.get_course_by_id(enrollment.course_id)
        if not course:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

        # prevent duplicate enrollment
        if self.enrollment_repository.check_enrollment_exists(enrollment.student_id, enrollment.course_id):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Already enrolled")

        return self.enrollment_repository.create_enrollment(enrollment)

    def get_all_enrollments(self):
        return self.enrollment_repository.get_all_enrollments()

    def get_enrollments_by_student(self, student_id: int):
        student = self.student_repository.get_student_by_id(student_id)
        if not student:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
        enrollments = self.enrollment_repository.get_enrollments_by_student(student_id)
        return [{"course_id": e.course_id, "course_title": e.course.title} for e in enrollments]

    def get_enrollments_by_course(self, course_id: int):
        course = self.course_repository.get_course_by_id(course_id)
        if not course:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
        return self.enrollment_repository.get_enrollments_by_course(course_id)