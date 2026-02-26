from sqlalchemy.orm import Session
from app.repositories.application_repository import ApplicationRepository
from app.repositories.job_repository import JobRepository
from app.repositories.user_repository import UserRepository
from app.exceptions.custom_exceptions import (
    ApplicationNotFoundException,
    JobNotFoundException,
    UserNotFoundException,
    AlreadyAppliedException
)

class ApplicationService:
    def __init__(self, db: Session):
        self.app_repo = ApplicationRepository(db)
        self.job_repo = JobRepository(db)
        self.user_repo = UserRepository(db)

    def apply_for_job(self, application_data: dict):
        user_id = application_data["user_id"]
        job_id = application_data["job_id"]

        # Business rule: validate user exists before applying
        user = self.user_repo.get_user_by_id(user_id)
        if not user:
            raise UserNotFoundException(user_id)

        # Business rule: validate job exists before applying
        job = self.job_repo.get_job_by_id(job_id)
        if not job:
            raise JobNotFoundException(job_id)

        # Business rule: prevent duplicate application
        existing = self.app_repo.get_existing_application(user_id, job_id)
        if existing:
            raise AlreadyAppliedException(user_id, job_id)

        return self.app_repo.create_application(application_data)

    def get_application(self, application_id: int):
        app = self.app_repo.get_application_by_id(application_id)
        if not app:
            raise ApplicationNotFoundException(application_id)
        return app

    def get_user_applications(self, user_id: int):
        # Nested query: GET /users/{user_id}/applications
        user = self.user_repo.get_user_by_id(user_id)
        if not user:
            raise UserNotFoundException(user_id)
        return self.app_repo.get_applications_by_user(user_id)