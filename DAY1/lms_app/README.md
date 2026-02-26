# LMS - Learning Management System

## Overview
An EdTech platform that manages Courses, Students, and Course Enrollments.
Built using FastAPI following Clean Architecture principles.

## Tech Stack
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## Folder Structure
lms_app/
│
├── app/
│   ├── main.py
│   ├── core/
│   │   └── db.py
│   ├── models/
│   │   ├── student_model.py
│   │   ├── course_model.py
│   │   └── enrollment_model.py
│   ├── schemas/
│   │   ├── student_schema.py
│   │   ├── course_schema.py
│   │   └── enrollment_schema.py
│   ├── repositories/
│   │   ├── student_repository.py
│   │   ├── course_repository.py
│   │   └── enrollment_repository.py
│   ├── services/
│   │   ├── student_service.py
│   │   ├── course_service.py
│   │   └── enrollment_service.py
│   ├── controllers/
│   │   ├── student_controller.py
│   │   ├── course_controller.py
│   │   └── enrollment_controller.py
│   ├── dependencies/
│   │   └── dependencies.py
│   └── middleware/
│       └── cors.py
│
├── requirements.txt
└── README.md

## Setup
```bash
python -m venv venv
venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run
```bash
uvicorn app.main:app --reload
```

## Swagger Docs
```
http://localhost:8000/docs
```

## Architecture Flow
Client → Controller → Service → Repository → Database

## API Endpoints

### Course APIs
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /courses | Create Course |
| GET | /courses | List All Courses |
| GET | /courses/{course_id} | Get Course by ID |

### Student APIs
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /students | Register Student |
| GET | /students/{student_id} | Get Student by ID |

### Enrollment APIs
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /enrollments | Enroll Student in Course |
| GET | /enrollments | Get All Enrollments |
| GET | /students/{student_id}/enrollments | Get Enrollments by Student |
| GET | /courses/{course_id}/enrollments | Get Enrollments by Course |

## HTTP Status Codes
| Scenario | Status Code |
|----------|-------------|
| Successful creation | 201 |
| Successful fetch | 200 |
| Invalid input | 422 |
| Not found | 404 |
| Duplicate enrollment | 400 |
