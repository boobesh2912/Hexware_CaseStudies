from sqlalchemy.orm import Session
from app.models.leave_request import LeaveRequest
from app.models.user import User

def create_leave(db: Session, leave_data: dict) -> LeaveRequest:
    db_leave = LeaveRequest(**leave_data)
    db.add(db_leave)
    db.commit()
    db.refresh(db_leave)
    return db_leave

def get_leave_by_id(db: Session, leave_id: int) -> LeaveRequest:
    return db.query(LeaveRequest).filter(LeaveRequest.id == leave_id).first()

def get_leaves_by_employee(db: Session, employee_id: int):
    return db.query(LeaveRequest).filter(LeaveRequest.employee_id == employee_id)

def get_all_leaves(db: Session):
    return db.query(LeaveRequest)

def update_leave(db: Session, leave: LeaveRequest, update_data: dict):
    for key, value in update_data.items():
        setattr(leave, key, value)
    db.commit()
    db.refresh(leave)
    return leave