from sqlalchemy.orm import Session
from app.repositories.job_repository import JobRepository
from app.exceptions.custom_exceptions import JobNotFoundException

class JobService:
    def __init__(self, db: Session):
        self.job_repo = JobRepository(db)

    def create_job(self, job_data: dict):
        return self.job_repo.create_job(job_data)

    def get_job(self, job_id: int):
        job = self.job_repo.get_job_by_id(job_id)
        if not job:
            raise JobNotFoundException(job_id)
        return job

    def get_all_jobs(self, skip: int = 0, limit: int = 10):
        # PDF: Support pagination for large datasets
        return self.job_repo.get_all_jobs(skip, limit)

    def update_job(self, job_id: int, update_data: dict):
        job = self.get_job(job_id)
        return self.job_repo.update_job(job, update_data)

    def delete_job(self, job_id: int):
        job = self.get_job(job_id)
        self.job_repo.delete_job(job)