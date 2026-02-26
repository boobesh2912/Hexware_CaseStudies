from sqlalchemy.orm import Session
from app.services.leave_service import apply_leave_service, list_employee_leaves_service

class EmployeeController:
    @staticmethod
    def apply_leave(db: Session, user, data: dict):
        return apply_leave_service(db, user, data)

    @staticmethod
    def get_my_leaves(db: Session, user, page: int, size: int):
        return list_employee_leaves_service(db, user.id, page, size)