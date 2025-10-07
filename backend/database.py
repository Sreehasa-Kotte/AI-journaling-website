# backend/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database file will be created in the backend folder
DATABASE_URL = "sqlite:///./journal.db"

# Create engine
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}  # required for SQLite
)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()
