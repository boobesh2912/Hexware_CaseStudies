from fastapi import FastAPI
from app.core.config import APP_NAME, VERSION
from app.middleware.cors import add_cors_middleware
from app.controllers.loan_controller import router as loan_router

app = FastAPI(
    title=APP_NAME,
    version=VERSION,
    description="Loan Application & Approval Management System API"
)

add_cors_middleware(app)

app.include_router(loan_router)

@app.get("/")
def root():
    return {"message": f"{APP_NAME} v{VERSION} is running"}
