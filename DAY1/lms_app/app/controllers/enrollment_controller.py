from fastapi import APIRouter, Depends, status
from typing import List
from app.schemas.enrollment_schema import EnrollmentCreate, EnrollmentResponse, EnrollmentByStudentResponse
from app.services.enrollment_service import EnrollmentService
from app.dependencies.dependencies import get_enrollment_service

router = APIRouter()


@router.post("/enrollments", response_model=EnrollmentResponse, status_code=status.HTTP_201_CREATED)
def enroll_student(enrollment: EnrollmentCreate, enrollment_service: EnrollmentService = Depends(get_enrollment_service)):
    return enrollment_service.enroll_student(enrollment)


@router.get("/enrollments", response_model=List[EnrollmentResponse], status_code=status.HTTP_200_OK)
def get_all_enrollments(enrollment_service: EnrollmentService = Depends(get_enrollment_service)):
    return enrollment_service.get_all_enrollments()


@router.get("/students/{student_id}/enrollments", response_model=List[EnrollmentByStudentResponse], status_code=status.HTTP_200_OK)
def get_enrollments_by_student(student_id: int, enrollment_service: EnrollmentService = Depends(get_enrollment_service)):
    return enrollment_service.get_enrollments_by_student(student_id)


@router.get("/courses/{course_id}/enrollments", response_model=List[EnrollmentResponse], status_code=status.HTTP_200_OK)
def get_enrollments_by_course(course_id: int, enrollment_service: EnrollmentService = Depends(get_enrollment_service)):
    return enrollment_service.get_enrollments_by_course(course_id)