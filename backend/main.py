from fastapi import FastAPI
from routes import journal
from database import Base, engine

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Journal Backend")

# Include routes
app.include_router(journal.router)

@app.get("/")
def home():
    return {"message": "Welcome to AI Journal API!"}
