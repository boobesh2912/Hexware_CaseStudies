# Enterprise Leave Management System (ELMS) - Backend

## Overview
ELMS is a robust backend system designed for a mid-size IT company to manage employee leave requests efficiently. It follows a strictly **Layered Architecture** and implements **Role-Based Access Control (RBAC)** to ensure secure and organized workflow management between Employees, Managers, and Administrators.

## 🚀 Tech Stack
* **Framework:** FastAPI (Python 3.11+)
* **ORM:** SQLAlchemy 2.0
* **Database:** PostgreSQL (Production/Dev), SQLite (Testing)
* **Migrations:** Alembic
* **Security:** JWT (JSON Web Tokens) & Bcrypt Password Hashing
* **Testing:** Pytest & HTTPX

## 📂 Project Structure
Following the clean architecture pattern, the project is organized as follows:
- `app/core/`: Security, Pagination, and Global Config.
- `app/models/`: SQLAlchemy Database Models.
- `app/schemas/`: Pydantic Data Validation (V2).
- `app/repositories/`: Raw Database Queries.
- `app/services/`: Business Logic & Validation.
- `app/controllers/`: Thin bridge between Routers and Services.
- `app/routers/`: API Endpoints.
- `app/middleware/`: Logging and Global Exception Handling.
- `tests/`: Comprehensive Test Suite.

## 🛠️ Setup & Installation

### 1. Prerequisites
Ensure you have **PostgreSQL** installed and running. Create a database named `elms_db`.

### 2. Environment Setup
```powershell
# Create Virtual Environment
python -m venv venv

# Activate Environment
.\venv\Scripts\Activate.ps1

# Install Dependencies
pip install -r requirements.txt
3. Database Migrations
Configure your DATABASE_URL in the .env file, then run:

PowerShell
# Initialize database schema
alembic upgrade head
4. Run the Application
PowerShell
uvicorn app.main:app --reload
The API will be available at http://127.0.0.1:8000.

🧪 Testing
The system includes automated tests for Authentication and Leave workflows.

PowerShell
python -m pytest -v
🔐 RBAC Workflow & Swagger UI
Access the interactive documentation at /docs and follow this sequence for testing:

Admin Setup: Register a user with the role ADMIN.

Authentication: Use POST /auth/login to get a JWT token.

Authorize: Click the "Authorize" button in Swagger and enter Bearer <your_token>.

Organization Setup: As an Admin, create a Department using POST /admin/departments.

User Onboarding: Register Managers and Employees using the department_id created in the previous step.

Leave Management:

Employee: Use POST /employee/apply-leave.

Manager: Use PUT /manager/leaves/{id} to Approve/Reject requests within their department.

📄 Compliance
This project satisfies all requirements specified in the ELMS Case Study PDF, including:

Proper Layered Architecture.

JWT-based authentication.

Pagination for administrative reports.

Comprehensive error handling and logging middleware.