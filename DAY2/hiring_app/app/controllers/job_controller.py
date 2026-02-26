from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.services.job_service import JobService
from app.schemas.job_schema import JobCreate, JobUpdate, JobResponse

router = APIRouter(prefix="/jobs", tags=["Jobs"])

# POST /jobs
@router.post("/", response_model=JobResponse, status_code=status.HTTP_201_CREATED)
def create_job(job_data: JobCreate, db: Session = Depends(get_db)):
    service = JobService(db)
    return service.create_job(job_data.model_dump())

# GET /jobs?skip=0&limit=10 - Pagination as query params
@router.get("/", response_model=List[JobResponse], status_code=status.HTTP_200_OK)
def get_jobs(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    service = JobService(db)
    return service.get_all_jobs(skip, limit)

# GET /jobs/{job_id}
@router.get("/{job_id}", response_model=JobResponse, status_code=status.HTTP_200_OK)
def get_job(job_id: int, db: Session = Depends(get_db)):
    service = JobService(db)
    return service.get_job(job_id)

# PUT /jobs/{job_id}
@router.put("/{job_id}", response_model=JobResponse, status_code=status.HTTP_200_OK)
def update_job(job_id: int, job_data: JobUpdate, db: Session = Depends(get_db)):
    service = JobService(db)
    return service.update_job(job_id, job_data.model_dump())

# DELETE /jobs/{job_id}
@router.delete("/{job_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_job(job_id: int, db: Session = Depends(get_db)):
    service = JobService(db)
    service.delete_job(job_id)