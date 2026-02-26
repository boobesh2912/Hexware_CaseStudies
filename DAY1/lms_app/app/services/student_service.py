from fastapi import HTTPException, status
from app.repositories.student_repository import StudentRepository
from app.schemas.student_schema import StudentCreate


class StudentService:
    def __init__(self, student_repository: StudentRepository):
        self.student_repository = student_repository

    def register_student(self, student: StudentCreate):
        return self.student_repository.create_student(student)

    def get_student_by_id(self, student_id: int):
        student = self.student_repository.get_student_by_id(student_id)
        if not student:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
        return student