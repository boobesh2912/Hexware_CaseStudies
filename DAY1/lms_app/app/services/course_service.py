from fastapi import HTTPException, status
from app.repositories.course_repository import CourseRepository
from app.schemas.course_schema import CourseCreate


class CourseService:
    def __init__(self, course_repository: CourseRepository):
        self.course_repository = course_repository

    def create_course(self, course: CourseCreate):
        return self.course_repository.create_course(course)

    def get_course_by_id(self, course_id: int):
        course = self.course_repository.get_course_by_id(course_id)
        if not course:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")
        return course

    def get_all_courses(self):
        return self.course_repository.get_all_courses()