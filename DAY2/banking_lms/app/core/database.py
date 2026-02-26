from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Auto-create banking_lms database if it doesn't exist
default_url = f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/postgres"
default_engine = create_engine(default_url, isolation_level="AUTOCOMMIT")

with default_engine.connect() as conn:
    result = conn.execute(text("SELECT 1 FROM pg_database WHERE datname = 'banking_lms'"))
    if not result.fetchone():
        conn.execute(text("CREATE DATABASE banking_lms"))

default_engine.dispose()

DATABASE_URL = settings.database_url
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()