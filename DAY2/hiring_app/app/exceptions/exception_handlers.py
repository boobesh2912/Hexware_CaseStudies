from fastapi import Request
from fastapi.responses import JSONResponse
from app.exceptions.custom_exceptions import (
    UserNotFoundException,
    UserAlreadyExistsException,
    JobNotFoundException,
    ApplicationNotFoundException,
    AlreadyAppliedException
)

# Each handler receives the request and the exception
# Returns a consistent JSON structure - same format every time

async def user_not_found_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(status_code=404, content={"detail": str(exc)})

async def user_already_exists_handler(request: Request, exc: UserAlreadyExistsException):
    return JSONResponse(status_code=400, content={"detail": str(exc)})

async def job_not_found_handler(request: Request, exc: JobNotFoundException):
    return JSONResponse(status_code=404, content={"detail": str(exc)})

async def application_not_found_handler(request: Request, exc: ApplicationNotFoundException):
    return JSONResponse(status_code=404, content={"detail": str(exc)})

async def already_applied_handler(request: Request, exc: AlreadyAppliedException):
    return JSONResponse(status_code=400, content={"detail": str(exc)})