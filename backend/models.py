from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from database import Base

class journal(Base):
    __tablename__ = "journal"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
