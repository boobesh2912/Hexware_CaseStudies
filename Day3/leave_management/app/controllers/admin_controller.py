from sqlalchemy.orm import Session
from app.services.department_service import create_department_service, list_departments_service
from app.services.user_service import list_all_users_service

class AdminController:
    @staticmethod
    def create_department(db: Session, data: dict):
        return create_department_service(db, data)

    @staticmethod
    def get_departments(db: Session):
        return list_departments_service(db)

    @staticmethod
    def get_all_users(db: Session, page: int, size: int):
        return list_all_users_service(db, page, size)