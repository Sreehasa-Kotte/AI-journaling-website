from pydantic import BaseModel

# Schema for creating a journal
class JournalCreate(BaseModel):
    title: str
    content: str

# Schema for returning a journal
class JournalResponse(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        orm_mode = True  # Important for SQLAlchemy models
