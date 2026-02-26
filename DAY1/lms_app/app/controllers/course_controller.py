from fastapi import APIRouter, Depends, status
from typing import List
from app.schemas.course_schema import CourseCreate, CourseResponse
from app.services.course_service import CourseService
from app.dependencies.dependencies import get_course_service

router = APIRouter()


@router.post("/courses", response_model=CourseResponse, status_code=status.HTTP_201_CREATED)
def create_course(course: CourseCreate, course_service: CourseService = Depends(get_course_service)):
    return course_service.create_course(course)


@router.get("/courses", response_model=List[CourseResponse], status_code=status.HTTP_200_OK)
def get_all_courses(course_service: CourseService = Depends(get_course_service)):
    return course_service.get_all_courses()


@router.get("/courses/{course_id}", response_model=CourseResponse, status_code=status.HTTP_200_OK)
def get_course(course_id: int, course_service: CourseService = Depends(get_course_service)):
    return course_service.get_course_by_id(course_id)