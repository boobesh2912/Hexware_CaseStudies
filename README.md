# Hexaware Technologies — FastAPI Training Projects

This repository contains all backend projects built during the Hexaware Technologies internship training program.
All projects follow **Clean Architecture** principles using **FastAPI + Python**.

---

## Repository Structure

```
projects/
├── Day_1/
│   ├── event_management_api/
│   ├── lms_app/
│   └── loan_app/
│
└── Day_2/
    ├── hiring_app/
    └── banking_lms/
```

---

## Quick Links

| Project | Day | README |
|---------|-----|--------|
| Event Management API | Day 1 | [📄 README](Day_1/event_management_api/README.md) |
| LMS — Learning Management System | Day 1 | [📄 README](Day_1/lms_app/README.md) |
| Loan Application & Approval | Day 1 | [📄 README](Day_1/loan_app/README.md) |
| Hiring Application Backend | Day 2 | [📄 README](Day_2/hiring_app/README.md) |
| Banking Loan Management System | Day 2 | [📄 README](Day_2/banking_lms/README.md) |

---

## Day 1 Projects

### 1. Event Management System API
**Folder:** `Day_1/event_management_api/` — [📄 View README](Day_1/event_management_api/README.md)

A REST API for managing events and participant registrations.

**Tech Stack:** FastAPI, Pydantic, In-Memory Storage (no DB)

**Key Features:**
- Create and list events with location filtering
- Register participants with capacity and duplicate checks
- Full business rule validation in service layer

**API Endpoints:**

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /events | Create event |
| GET | /events | List all events |
| GET | /events?location=Chennai | Filter by location |
| GET | /events/{id} | Get event by ID |
| POST | /participants | Register participant |
| GET | /participants/{id} | Get participant by ID |

**Business Rules:**
- Duplicate event names not allowed
- Participant email must be unique
- Event must exist before registering participant
- Event capacity must not be exceeded

**Run:**
```bash
cd Day_1/event_management_api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

### 2. LMS — Learning Management System
**Folder:** `Day_1/lms_app/` — [📄 View README](Day_1/lms_app/README.md)

An EdTech platform for managing Courses, Students, and Enrollments.

**Tech Stack:** FastAPI, SQLAlchemy, SQLite, Pydantic

**Key Features:**
- Student registration and lookup
- Course creation and listing
- Student-to-course enrollment with duplicate prevention
- Nested routes for enrollments by student and by course

**Database Schema:**
```
Student 1 ---- * Enrollment * ---- 1 Course
```

**API Endpoints:**

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /students | Register student |
| GET | /students/{id} | Get student |
| POST | /courses | Create course |
| GET | /courses | List courses |
| GET | /courses/{id} | Get course |
| POST | /enrollments | Enroll student |
| GET | /enrollments | List all enrollments |
| GET | /students/{id}/enrollments | Enrollments by student |
| GET | /courses/{id}/enrollments | Enrollments by course |

**Business Rules:**
- Student and course must exist before enrollment
- Duplicate enrollment prevented

**Run:**
```bash
cd Day_1/lms_app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

### 3. Loan Application & Approval System
**Folder:** `Day_1/loan_app/` — [📄 View README](Day_1/loan_app/README.md)

A simple loan application and approval API with eligibility validation.

**Tech Stack:** FastAPI, Pydantic, In-Memory Storage (no DB)

**Key Features:**
- Submit loan applications with eligibility check
- Approve or reject pending applications
- Frontend HTML interface included

**API Endpoints:**

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /loans | Submit application |
| GET | /loans | List all applications |
| GET | /loans/{id} | Get by ID |
| PUT | /loans/{id}/approve | Approve loan |
| PUT | /loans/{id}/reject | Reject loan |

**Business Rules:**
- Loan amount must be ≤ income × 10
- Only PENDING loans can be approved or rejected

**Run:**
```bash
cd Day_1/loan_app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
> Open `frontend.html` in browser after starting the server.

---

## Day 2 Projects

### 4. Hiring Application Backend
**Folder:** `Day_2/hiring_app/` — [📄 View README](Day_2/hiring_app/README.md)

Enterprise-grade backend for managing job postings, users, and job applications.

**Tech Stack:** FastAPI, PostgreSQL, SQLAlchemy ORM, Alembic, Pydantic

**Key Features:**
- Full user management with role-based design (admin/recruiter/candidate)
- Job CRUD with pagination
- Job application with duplicate prevention
- Custom exception handling with central handlers
- CORS + Logging middleware
- Alembic migrations
- Password hashing

**Database Schema:**
```
User 1 ---- * Application * ---- 1 Job
```

**API Endpoints:**

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /users/ | Create user |
| GET | /users/ | List users (pagination) |
| GET | /users/{id} | Get user |
| PUT | /users/{id} | Update user |
| DELETE | /users/{id} | Delete user |
| POST | /jobs/ | Create job |
| GET | /jobs/?skip=0&limit=10 | List jobs (pagination) |
| GET | /jobs/{id} | Get job |
| PUT | /jobs/{id} | Update job |
| DELETE | /jobs/{id} | Delete job |
| POST | /applications | Apply for job |
| GET | /applications/{id} | View application |
| GET | /users/{id}/applications | Applications by user |

**Run:**
```bash
cd Day_2/hiring_app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
# Create app/.env with DB credentials
psql -U postgres -c "CREATE DATABASE hiringdb;"
alembic revision --autogenerate -m "initial schema"
alembic upgrade head
uvicorn app.main:app --reload
```

---

### 5. Banking Loan Management System (LMS)
**Folder:** `Day_2/banking_lms/` — [📄 View README](Day_2/banking_lms/README.md)

Enterprise banking backend for managing loan products, applications, and repayments with strict transactional integrity.

**Tech Stack:** FastAPI, PostgreSQL, SQLAlchemy ORM, Alembic, Pydantic

**Key Features:**
- User management with roles (admin/loan_officer/customer)
- Loan product management
- Full loan lifecycle: pending → approved → disbursed → closed
- Repayment tracking with auto loan closure
- Strict business rule enforcement in service layer
- Custom exception handling
- CORS + Logging middleware
- Alembic migrations
- Pytest test suite (31 tests)

**Database Schema:**
```
Customer (User)  1 ---- * LoanApplication
LoanOfficer      1 ---- * LoanApplication
LoanProduct      1 ---- * LoanApplication
LoanApplication  1 ---- * Repayment
```

**API Endpoints:**

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /users/ | Create user |
| GET | /users/ | List users |
| GET | /users/{id} | Get user |
| PUT | /users/{id} | Update user |
| DELETE | /users/{id} | Delete user |
| POST | /loan-products/ | Create product |
| GET | /loan-products/ | List products (pagination) |
| GET | /loan-products/{id} | Get product |
| PUT | /loan-products/{id} | Update product |
| DELETE | /loan-products/{id} | Delete product |
| POST | /loan-applications/ | Apply for loan |
| GET | /loan-applications/ | List applications (pagination) |
| GET | /loan-applications/{id} | Get application |
| PUT | /loan-applications/{id}/status | Approve / Reject / Disburse |
| POST | /repayments | Add repayment |
| GET | /loan-applications/{id}/repayments | Repayment history |

**Business Rules:**
- Loan amount cannot exceed product `max_amount`
- Only `loan_officer` role can approve or reject
- Cannot disburse unless status is `approved`
- Loan auto-closes after total repayments ≥ `approved_amount`
- Repayments only allowed on `disbursed` loans
- All financial operations use commit/rollback transactions

**Run:**
```bash
cd Day_2/banking_lms
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
# Create app/.env with DB credentials
psql -U postgres -c "CREATE DATABASE banking_lms;"
alembic revision --autogenerate -m "initial schema"
alembic upgrade head
uvicorn app.main:app --reload
```

**Run Tests:**
```bash
pytest -v
```

---

## Architecture Pattern (Day 2 Projects)

All Day 2 projects follow strict Clean Architecture:

```
Client
  ↓
Controller  →  HTTP only, Pydantic validation
  ↓
Service     →  Business logic, custom exceptions
  ↓
Repository  →  Raw DB queries, SQLAlchemy
  ↓
PostgreSQL
```

## Architecture Pattern (Day 1 Projects)

Day 1 projects use the same layered pattern but with simpler storage:
- `event_management_api` and `loan_app` use **in-memory storage** (no DB)
- `lms_app` uses **SQLite** via SQLAlchemy

---

## Common Setup for All Projects

```bash
# 1. Navigate into the project folder
cd Day_X/project_name

# 2. Create virtual environment
python -m venv venv

# 3. Activate
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# 4. Install dependencies
pip install -r requirements.txt

# 5. Start server
uvicorn app.main:app --reload
```

Swagger UI always available at: **http://localhost:8000/docs**
