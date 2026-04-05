from fastapi import FastAPI
from db import Base,engine
from router import login,reg,transaction, update, delete, filtering, summary

Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(reg.router)
app.include_router(login.router)
app.include_router(transaction.router)
app.include_router(update.router, tags=["Update"])
app.include_router(delete.router, tags=["Delete"])
app.include_router(filtering.router, tags=["Filtering"])
app.include_router(summary.router, tags=["Analytics"])
@app.get("/")
def root():
    return {
        "message": "Finance Tracker API is running"
    }