from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from pydantic import BaseModel
from models import journal  # <-- This imports the SQLAlchemy model
from schemas import JournalCreate
from schemas import JournalResponse

router = APIRouter(prefix="/journals", tags=["journals"])

# Pydantic model for request body
class JournalCreate(BaseModel):
    title: str
    content: str

# Get all journals
@router.get("/")
def read_journals(db: Session = Depends(get_db)):
    return db.query(journal).all()

# Get single journal by ID
@router.get("/{journal_id}")
def read_journal(journal_id: int, db: Session = Depends(get_db)):
    journal_item = db.query(journal).filter(journal.id == journal_id).first()
    if not journal_item:
        raise HTTPException(status_code=404, detail="Journal not found")
    return journal_item

# Create a new journal
@router.post("/", response_model=JournalResponse)
def create_journal(journal_data: JournalCreate, db: Session = Depends(get_db)):
    new_journal = journal(title=journal_data.title, content=journal_data.content)
    db.add(new_journal)
    db.commit()
    db.refresh(new_journal)
    return new_journal

# Update a journal
@router.put("/{journal_id}", response_model=JournalResponse)
def update_journal(journal_id: int, journal_data: JournalCreate, db: Session = Depends(get_db)):
    journal_item = db.query(journal).filter(journal.id == journal_id).first()
    if not journal_item:
        raise HTTPException(status_code=404, detail="Journal not found")
    journal_item.title = journal_data.title
    journal_item.content = journal_data.content

    db.commit()
    db.refresh(journal_item)
    return journal_item

# Delete a journal
@router.delete("/{journal_id}")
def delete_journal(journal_id: int, db: Session = Depends(get_db)):
    existing = db.query(journal).filter(journal.id == journal_id).first()
    if not existing:
        raise HTTPException(status_code=404, detail="Journal not found")
    db.delete(existing)
    db.commit()
    return {"detail": "Journal deleted"}
