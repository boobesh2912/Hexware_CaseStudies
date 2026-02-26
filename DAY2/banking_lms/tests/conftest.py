import sys
import os

# Add project root to Python path so imports work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.core.database import Base, get_db
from app.main import app

# Use SQLite for testing - no need for PostgreSQL to be running
# This is an in-memory DB, created fresh for every test run
TEST_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False}  # needed for SQLite only
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create all tables in test DB
Base.metadata.create_all(bind=engine)

# Override get_db to use test DB instead of real PostgreSQL
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

# client fixture - shared across all test files
@pytest.fixture()
def client():
    return TestClient(app)