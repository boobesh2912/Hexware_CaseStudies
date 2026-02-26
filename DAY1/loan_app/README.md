# Loan Application & Approval Management System

## Setup & Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `frontend.html` in your browser while uvicorn is running.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /loans | Submit application |
| GET | /loans | List all applications |
| GET | /loans/{id} | Get by ID |
| PUT | /loans/{id}/approve | Approve loan |
| PUT | /loans/{id}/reject | Reject loan |

## Business Rules
- Loan amount ≤ income × 10
- Only PENDING loans can be approved/rejected

## Swagger Docs
http://localhost:8000/docs
