from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models import User, Transaction
from schema import TransactionSchema

router = APIRouter(prefix="/transactions")

@router.post("/")
def create_transaction(data: TransactionSchema, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == data.user_id).first()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid user")

    transaction = Transaction(
        user_id=user.id,
        amount=data.amount,
        type=data.type,
        category=data.category,
        note=data.note,
        date=data.date
    )

    db.add(transaction)
    db.commit()

    return {
        "message": "Transaction added"
    }