# backend/routes/journals.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import JournalEntry

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get all journal entries
@router.get("/journals")
def get_journals(db: Session = Depends(get_db)):
    return db.query(JournalEntry).all()

# Create a new journal entry
@router.post("/journals")
def create_journal(title: str = None, content: str = "", mood: str = None, db: Session = Depends(get_db)):
    new_entry = JournalEntry(title=title, content=content, mood=mood)
    db.add(new_entry)
    db.commit()
    db.refresh(new_entry)
    return new_entry
