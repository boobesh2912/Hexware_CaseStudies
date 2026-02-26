# Hiring Application - Backend API

Enterprise-grade FastAPI backend for managing job postings, user accounts, and job applications.

---

## Tech Stack

- **Python** + **FastAPI**
- **PostgreSQL** + **SQLAlchemy ORM**
- **Alembic** for migrations
- **Pydantic** for validation

---

## Folder Structure

```
hiring_app/
├── app/
│   ├── main.py
│   ├── .env
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   └── logger.py
│   ├── models/
│   │   ├── base.py
│   │   ├── user.py
│   │   ├── job.py
│   │   └── application.py
│   ├── schemas/
│   │   ├── user_schema.py
│   │   ├── job_schema.py
│   │   └── application_schema.py
│   ├── repositories/
│   │   ├── user_repository.py
│   │   ├── job_repository.py
│   │   └── application_repository.py
│   ├── services/
│   │   ├── user_service.py
│   │   ├── job_service.py
│   │   └── application_service.py
│   ├── controllers/
│   │   ├── user_controller.py
│   │   ├── job_controller.py
│   │   └── application_controller.py
│   ├── middleware/
│   │   ├── cors.py
│   │   └── logging.py
│   └── exceptions/
│       ├── custom_exceptions.py
│       └── exception_handlers.py
├── alembic/
├── alembic.ini
├── requirements.txt
└── README.md
```

---

## Architecture Flow

```
Client
  ↓
Controller  →  validates request (Pydantic)
  ↓
Service     →  business logic, raises custom exceptions
  ↓
Repository  →  raw DB operations (SQLAlchemy)
  ↓
PostgreSQL
```

---

## Database Schema

**Users** — id, name, email (unique), role (admin/recruiter/candidate), hashed_password

**Jobs** — id, title, description, salary, company_id

**Applications** — id, user_id (FK), job_id (FK), status (applied/shortlisted/rejected)

```
User 1 ------- * Application * ------- 1 Job
```

---

## Setup & Run

### 1. Clone the repo
```bash
git clone https://github.com/your-username/hiring_app.git
cd hiring_app
```

### 2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment
Create `app/.env`:
```
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=your_password
DB_NAME=hiringdb
```

### 5. Create database (one time only)
```bash
psql -U postgres -c "CREATE DATABASE hiringdb;"
```

### 6. Run Alembic migrations
```bash
alembic revision --autogenerate -m "initial schema"
alembic upgrade head
```

### 7. Start the server
```bash
uvicorn app.main:app --reload
```

### 8. Open Swagger docs
```
http://localhost:8000/docs
```

---

## API Endpoints

### Users
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /users/ | Create user |
| GET | /users/ | List users (pagination) |
| GET | /users/{user_id} | Get user |
| PUT | /users/{user_id} | Update user |
| DELETE | /users/{user_id} | Delete user |

### Jobs
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /jobs/ | Create job |
| GET | /jobs/?skip=0&limit=10 | List jobs (pagination) |
| GET | /jobs/{job_id} | Get job |
| PUT | /jobs/{job_id} | Update job |
| DELETE | /jobs/{job_id} | Delete job |

### Applications
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /applications | Apply for job |
| GET | /applications/{id} | View application |
| GET | /users/{user_id}/applications | All applications by user |

---

## Sample Request

**Create Job**
```json
POST /jobs/
{
  "title": "Backend Developer",
  "description": "FastAPI + PostgreSQL",
  "salary": 120000,
  "company_id": 1
}
```

**Apply for Job**
```json
POST /applications
{
  "user_id": 1,
  "job_id": 1
}
```