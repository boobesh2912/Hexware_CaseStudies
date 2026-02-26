from fastapi import APIRouter, Depends, status
from app.schemas.student_schema import StudentCreate, StudentResponse
from app.services.student_service import StudentService
from app.dependencies.dependencies import get_student_service

router = APIRouter()


@router.post("/students", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def register_student(student: StudentCreate, student_service: StudentService = Depends(get_student_service)):
    return student_service.register_student(student)


@router.get("/students/{student_id}", response_model=StudentResponse, status_code=status.HTTP_200_OK)
def get_student(student_id: int, student_service: StudentService = Depends(get_student_service)):
    return student_service.get_student_by_id(student_id)