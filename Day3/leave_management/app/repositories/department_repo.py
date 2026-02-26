from sqlalchemy.orm import Session
from app.models.department import Department

def create_department(db: Session, dept_data: dict) -> Department:
    db_dept = Department(**dept_data)
    db.add(db_dept)
    db.commit()
    db.refresh(db_dept)
    return db_dept

def get_department_by_id(db: Session, dept_id: int) -> Department:
    return db.query(Department).filter(Department.id == dept_id).first()

def get_all_departments(db: Session):
    return db.query(Department)

def delete_department(db: Session, dept: Department):
    db.delete(dept)
    db.commit()