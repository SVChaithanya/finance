from models import Transaction
from db import get_db
from sqlalchemy.orm import Session
from fastapi import APIRouter,HTTPException,Depends
from datetime import datetime


router = APIRouter(prefix="/filtering")

@router.get("/transactions")
def get_transactions(
    user_id: str,
    type: str | None = None,
    category: str | None = None,
    date: str | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(Transaction).filter(Transaction.user_id == user_id)

    if type:
        query = query.filter(Transaction.type == type)

    if category:
        query = query.filter(Transaction.category == category)

    if date:
        query = query.filter(Transaction.date == date)

    results = query.all()

    return results