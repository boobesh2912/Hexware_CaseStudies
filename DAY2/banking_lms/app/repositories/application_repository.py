from sqlalchemy.orm import Session
from app.models.loan_application import LoanApplication

class ApplicationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_application(self, application_data: dict) -> LoanApplication:
        new_app = LoanApplication(**application_data)
        self.db.add(new_app)
        self.db.commit()
        self.db.refresh(new_app)
        return new_app

    def get_application_by_id(self, application_id: int) -> LoanApplication:
        return self.db.query(LoanApplication).filter(LoanApplication.id == application_id).first()

    def get_all_applications(self, skip: int = 0, limit: int = 10):
        return self.db.query(LoanApplication).offset(skip).limit(limit).all()

    def update_status(self, application: LoanApplication, update_data: dict) -> LoanApplication:
        for key, value in update_data.items():
            if value is not None:
                setattr(application, key, value)
        try:
            self.db.commit()
        except:
            self.db.rollback()
            raise
        self.db.refresh(application)
        return application