from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# Step 1: Connect to default 'postgres' DB to check/create 'hiringdb'
# We can't connect to hiringdb if it doesn't exist yet
default_url = f"postgresql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/postgres"
default_engine = create_engine(default_url, isolation_level="AUTOCOMMIT")

with default_engine.connect() as conn:
    result = conn.execute(text("SELECT 1 FROM pg_database WHERE datname = 'hiringdb'"))
    if not result.fetchone():
        conn.execute(text("CREATE DATABASE hiringdb"))

default_engine.dispose()

# Step 2: Now connect to hiringdb normally
DATABASE_URL = settings.database_url
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency Injection - used in every controller via Depends(get_db)
def get_db():
    db = SessionLocal()
    try:
        yield db       # yield gives the session to the route handler
    finally:
        db.close()     # always closes after request finishes - prevents connection leaks