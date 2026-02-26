# Event Management System API

A backend REST API for managing events and participants built with **FastAPI** following Clean Architecture principles.

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- In-Memory Storage (V1.0)

## Folder Structure

```
event_management_api/
│
├── app/
│   ├── main.py
│   │
│   ├── core/
│   │   └── db.py
│   │
│   ├── controllers/
│   │   ├── event_controller.py
│   │   └── participant_controller.py
│   │
│   ├── services/
│   │   ├── event_service.py
│   │   └── participant_service.py
│   │
│   ├── repositories/
│   │   ├── event_repository.py
│   │   └── participant_repository.py
│   │
│   ├── schemas/
│   │   ├── event_schema.py
│   │   └── participant_schema.py
│   │
│   ├── dependencies/
│   │   └── service_dependency.py
│   │
│   └── middleware/
│       └── cors_middleware.py
│
├── .env
├── requirements.txt
└── README.md
```

## Setup & Run

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn app.main:app --reload
```

Swagger UI: **http://localhost:8000/docs**

## API Endpoints

### Event APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /events | Create a new event |
| GET | /events | List all events |
| GET | /events/{event_id} | Get event by ID |
| GET | /events?location=Chennai | Filter events by location |

### Participant APIs

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /participants | Register a participant |
| GET | /participants/{id} | Get participant by ID |

## Sample Requests

**Create Event**
```json
POST /events
{
  "name": "Python Workshop",
  "location": "Chennai",
  "capacity": 100
}
```

**Register Participant**
```json
POST /participants
{
  "name": "Boobesh",
  "email": "boobesh@email.com",
  "event_id": 1
}
```

## Business Rules

- Duplicate event names are not allowed
- Participant email must be unique
- Event must exist before registering a participant
- Event capacity must not be exceeded

## Architecture

Each layer has a single responsibility:

- **Controllers** — Handle HTTP requests and responses only
- **Services** — All business logic and validation
- **Repositories** — Pure data access (CRUD)
- **Schemas** — Pydantic models for input/output validation
- **Dependencies** — Dependency injection wiring
