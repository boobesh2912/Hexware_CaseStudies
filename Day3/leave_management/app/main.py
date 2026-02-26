from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from app.database.base import Base
from app.database.session import engine
from app.routers import auth_router, admin_router, manager_router, employee_router
from app.middleware.logging import logging_middleware
from app.middleware.exception_handler import http_exception_handler, validation_exception_handler, global_exception_handler

app = FastAPI(title="Enterprise Leave Management System (ELMS)", version="1.0.0")

Base.metadata.create_all(bind=engine) # Initialize tables

app.middleware("http")(logging_middleware)
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.add_exception_handler(HTTPException, http_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, global_exception_handler)

app.include_router(auth_router.router)
app.include_router(admin_router.router)
app.include_router(manager_router.router)
app.include_router(employee_router.router)

@app.get("/")
def root():
    return {"message": "ELMS API is running"}