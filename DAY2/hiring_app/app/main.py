from fastapi import FastAPI

from app.core.database import engine, Base

# Import all models so Base.metadata knows about all tables
from app.models import user, job, application  # noqa: F401

from app.middleware.cors import setup_cors
from app.middleware.logging import LoggingMiddleware

from app.exceptions.exception_handlers import (
    user_not_found_handler,
    user_already_exists_handler,
    job_not_found_handler,
    application_not_found_handler,
    already_applied_handler
)
from app.exceptions.custom_exceptions import (
    UserNotFoundException,
    UserAlreadyExistsException,
    JobNotFoundException,
    ApplicationNotFoundException,
    AlreadyAppliedException
)

from app.controllers import user_controller, job_controller, application_controller

app = FastAPI(title="Hiring Application API", version="1.0.0")

# Create all tables on startup
Base.metadata.create_all(bind=engine)

# Register middleware
setup_cors(app)
app.add_middleware(LoggingMiddleware)

# Register custom exception handlers
# When service raises UserNotFoundException, user_not_found_handler runs automatically
app.add_exception_handler(UserNotFoundException, user_not_found_handler)
app.add_exception_handler(UserAlreadyExistsException, user_already_exists_handler)
app.add_exception_handler(JobNotFoundException, job_not_found_handler)
app.add_exception_handler(ApplicationNotFoundException, application_not_found_handler)
app.add_exception_handler(AlreadyAppliedException, already_applied_handler)

# Register routers
app.include_router(user_controller.router)
app.include_router(job_controller.router)
app.include_router(application_controller.router)

@app.get("/")
def root():
    return {"message": "Hiring Application API is running"}