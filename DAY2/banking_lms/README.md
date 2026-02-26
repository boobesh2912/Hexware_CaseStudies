# Banking Loan Management System (LMS)

Enterprise FastAPI backend for managing loans, applications, and repayments.
Built as part of Hexaware Technologies internship training.

---

## Tech Stack
- FastAPI + Python
- PostgreSQL + SQLAlchemy ORM
- Alembic migrations
- Pydantic validation

---

## Folder Structure
```
banking_lms/
├── app/
│   ├── main.py
│   ├── .env
│   ├── core/          → config, database, logger
│   ├── models/        → user, loan_product, loan_application, repayment
│   ├── schemas/       → pydantic request/response models
│   ├── repositories/  → raw DB operations
│   ├── services/      → business logic
│   ├── controllers/   → API routes
│   ├── middleware/    → cors, logging
│   └── exceptions/    → custom exceptions + handlers
├── alembic/
├── alembic.ini
├── requirements.txt
```

---

## Setup & Run

```bash
# 1. Clone
git clone https://github.com/your-username/banking_lms.git
cd banking_lms

# 2. Virtual environment
python -m venv venv
venv\Scripts\activate

# 3. Install
pip install -r requirements.txt

# 4. Create .env inside app/
DB_HOST=localhost
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=your_password
DB_NAME=banking_lms

# 5. Create DB (one time)
psql -U postgres -c "CREATE DATABASE banking_lms;"

# 6. Alembic migrations
alembic revision --autogenerate -m "initial schema"
alembic upgrade head

# 7. Run
uvicorn app.main:app --reload
```

Open: http://localhost:8000/docs

---

## API Endpoints

### Users
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /users/ | Create user |
| GET | /users/ | List users |
| GET | /users/{id} | Get user |
| PUT | /users/{id} | Update user |
| DELETE | /users/{id} | Delete user |

### Loan Products
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /loan-products/ | Create product |
| GET | /loan-products/ | List (pagination) |
| GET | /loan-products/{id} | Get product |
| PUT | /loan-products/{id} | Update |
| DELETE | /loan-products/{id} | Delete |

### Loan Applications
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /loan-applications/ | Apply for loan |
| GET | /loan-applications/ | List (pagination) |
| GET | /loan-applications/{id} | Get application |
| PUT | /loan-applications/{id}/status | Approve/Reject/Disburse |

### Repayments
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /repayments | Add repayment |
| GET | /loan-applications/{id}/repayments | View repayment history |

---

## Business Rules
- Loan amount cannot exceed product `max_amount`
- Only `loan_officer` can approve/reject
- Cannot disburse unless status = `approved`
- Loan auto-closes after full repayment
- All financial operations are transactional