from fastapi import FastAPI
from app.core.db import Base, engine
from app.middleware.cors import add_cors_middleware
from app.controllers import student_controller, course_controller, enrollment_controller
from app.models import student_model, course_model, enrollment_model

app = FastAPI(title="LMS - Course Enrollment Platform")

# create all tables on startup
Base.metadata.create_all(bind=engine)

# register middleware
add_cors_middleware(app)

# include all routers
app.include_router(student_controller.router)
app.include_router(course_controller.router)
app.include_router(enrollment_controller.router)


@app.get("/")
def root():
    return {"message": "LMS API is running"}