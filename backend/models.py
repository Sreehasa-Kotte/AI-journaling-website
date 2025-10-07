# backend/models.py

from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from datetime import datetime

class JournalEntry(Base):
    __tablename__ = "journal_entries"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=True)
    content = Column(Text, nullable=False)
    mood = Column(String, nullable=True)
    ai_summary = Column(Text, nullable=True)
    date = Column(DateTime, default=datetime.utcnow)
