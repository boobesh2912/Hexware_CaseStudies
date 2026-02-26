# Hexaware Technologies — FastAPI Training Projects

This repository contains all backend projects built during the **Hexaware Technologies Internship Training Program**.

All projects follow **Clean Architecture principles** using:

* FastAPI
* Python
* SQLAlchemy
* PostgreSQL / SQLite
* Pydantic
* Alembic

---

## 📁 Repository Structure

```
projects/
├── Day_1/
│   ├── event_management_api/
│   ├── lms_app/
│   └── loan_app/
│
├── Day_2/
│   ├── hiring_app/
│   └── banking_lms/
│
└── Day_3/
    └── leave_management/
```

---

## 🚀 Quick Links

| Project | Day | README |
|----------|-----|--------|
| Event Management API | Day 1 | [📄 View](Day_1/event_management_api/README.md) |
| LMS — Learning Management System | Day 1 | [📄 View](Day_1/lms_app/README.md) |
| Loan Application & Approval | Day 1 | [📄 View](Day_1/loan_app/README.md) |
| Hiring Application Backend | Day 2 | [📄 View](Day_2/hiring_app/README.md) |
| Banking Loan Management System | Day 2 | [📄 View](Day_2/banking_lms/README.md) |
| Enterprise Leave Management (ELMS) | Day 3 | [📄 View](Day_3/leave_management/README.md) |

---

# 📅 Day 1 Projects

## 1️⃣ Event Management System API

**Folder:** `Day_1/event_management_api/`

A REST API for managing events and participant registrations.

### Tech Stack

* FastAPI
* Pydantic
* In-Memory Storage (No Database)

### Key Features

* Create and list events with location filtering
* Register participants with:

  * Capacity checks
  * Duplicate prevention
* Full business rule validation in Service Layer

### API Endpoints

| Method | Endpoint                   | Description           |
| ------ | -------------------------- | --------------------- |
| POST   | `/events`                  | Create event          |
| GET    | `/events`                  | List all events       |
| GET    | `/events?location=Chennai` | Filter by location    |
| GET    | `/events/{id}`             | Get event by ID       |
| POST   | `/participants`            | Register participant  |
| GET    | `/participants/{id}`       | Get participant by ID |

### Run

```bash
cd Day_1/event_management_api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 2️⃣ LMS — Learning Management System

**Folder:** `Day_1/lms_app/`

An EdTech backend for managing Courses, Students, and Enrollments.

### Tech Stack

* FastAPI
* SQLAlchemy
* SQLite
* Pydantic

### Database Schema

```
Student 1 ---- * Enrollment * ---- 1 Course
```

### Run

```bash
cd Day_1/lms_app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 3️⃣ Loan Application & Approval System

**Folder:** `Day_1/loan_app/`

A loan application system with eligibility validation logic.

### Tech Stack

* FastAPI
* Pydantic
* In-Memory Storage

### Run

```bash
cd Day_1/loan_app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

# 📅 Day 2 Projects

## 4️⃣ Hiring Application Backend

**Folder:** `Day_2/hiring_app/`

Enterprise-grade backend for managing job postings, users, and job applications.

### Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy ORM
* Alembic
* Pydantic

### Database Schema

```
User 1 ---- * Application * ---- 1 Job
```

### Run

```bash
cd Day_2/hiring_app
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Create .env file inside app/ with DB credentials
psql -U postgres -c "CREATE DATABASE hiringdb;"

alembic revision --autogenerate -m "initial schema"
alembic upgrade head

uvicorn app.main:app --reload
```

---

## 5️⃣ Banking Loan Management System

**Folder:** `Day_2/banking_lms/`

Enterprise banking backend managing loan products, applications, and repayments with strict transactional integrity.

### Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy ORM
* Alembic
* Pydantic
* Pytest

### Key Features

* User roles:

  * Admin
  * Loan Officer
  * Customer
* Full loan lifecycle:

```
pending → approved → disbursed → closed
```

* Repayment tracking
* Automatic loan closure
* 31 Pytest test cases

### Run

```bash
cd Day_2/banking_lms
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Create .env file inside app/ with DB credentials
psql -U postgres -c "CREATE DATABASE banking_lms;"

alembic revision --autogenerate -m "initial schema"
alembic upgrade head

uvicorn app.main:app --reload
```

---

# 📅 Day 3 Project

## 6️⃣ Enterprise Leave Management System (ELMS)

**Folder:** `Day_3/leave_management/`

Enterprise-grade backend for managing departments and leave workflows with strict Role-Based Access Control (RBAC).

### Tech Stack

* FastAPI
* SQLite
* SQLAlchemy 2.0
* Pydantic V2
* Alembic
* Pytest

### Key Features

* Advanced RBAC:

  * Admin → Full CRUD
  * Manager → Department approvals
  * Employee → Apply/View own leaves
* Overlap detection for leave dates
* Department isolation
* JWT authentication
* Bcrypt password hashing
* Strict Pydantic V2 validation

### API Endpoints

| Method | Endpoint                | Access   | Description          |
| ------ | ----------------------- | -------- | -------------------- |
| POST   | `/auth/register`        | Public   | Register user        |
| POST   | `/auth/login`           | Public   | Obtain JWT           |
| POST   | `/admin/departments`    | Admin    | Create department    |
| GET    | `/admin/users`          | Admin    | List workforce       |
| POST   | `/employee/apply-leave` | Employee | Submit leave         |
| PUT    | `/manager/leaves/{id}`  | Manager  | Approve/Reject leave |

### Run

```bash
cd Day_3/leave_management
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

alembic upgrade head
uvicorn app.main:app --reload
```

### Run Tests

```bash
python -m pytest -v
```

---

# 🏗 Architecture Pattern (Day 2 & 3)

All advanced projects follow strict Clean Architecture:

```
Client
  ↓
Router      → HTTP endpoints & Role-based dependencies
  ↓
Controller  → Thin mapping layer
  ↓
Service     → Business rules & validations
  ↓
Repository  → Database access (SQLAlchemy)
  ↓
Database    → PostgreSQL / SQLite
```

---

# 🏗 Architecture Pattern (Day 1)

Same layered structure but simplified storage:

* `event_management_api` → In-memory storage
* `loan_app` → In-memory storage
* `lms_app` → SQLite

---

# ⚙ Common Setup (All Projects)

```bash
# 1. Navigate to project
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

---

# 📘 API Documentation

Interactive Swagger UI available at:

```
http://localhost:8000/docs
```

Available for every running project.
