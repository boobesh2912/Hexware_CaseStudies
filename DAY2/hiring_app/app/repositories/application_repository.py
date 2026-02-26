from sqlalchemy.orm import Session
from app.models.application import Application

class ApplicationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_application(self, application_data: dict) -> Application:
        new_app = Application(**application_data)
        self.db.add(new_app)
        self.db.commit()
        self.db.refresh(new_app)
        return new_app

    def get_application_by_id(self, application_id: int) -> Application:
        return self.db.query(Application).filter(Application.id == application_id).first()

    def get_applications_by_user(self, user_id: int):
        # Nested query: GET /users/{user_id}/applications
        return self.db.query(Application).filter(Application.user_id == user_id).all()

    def get_existing_application(self, user_id: int, job_id: int) -> Application:
        # Check if user already applied for this job - prevents duplicates
        return self.db.query(Application).filter(
            Application.user_id == user_id,
            Application.job_id == job_id
        ).first()

    def update_status(self, application: Application, status: str) -> Application:
        application.status = status
        self.db.commit()
        self.db.refresh(application)
        return application