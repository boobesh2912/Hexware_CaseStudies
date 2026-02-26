from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repositories.department_repo import create_department, get_department_by_id, get_all_departments

def create_department_service(db: Session, data: dict):
    return create_department(db, data)

def list_departments_service(db: Session):
    return get_all_departments(db).all()

def get_department_service(db: Session, dept_id: int):
    dept = get_department_by_id(db, dept_id)
    if not dept:
        raise HTTPException(status_code=404, detail="Department not found")
    return dept