from sqlalchemy.orm import Session
from app.services.leave_service import approve_reject_leave_service

class ManagerController:
    @staticmethod
    def update_leave_status(db: Session, leave_id: int, status: str, manager):
        return approve_reject_leave_service(db, leave_id, status, manager)