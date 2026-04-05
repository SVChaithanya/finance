from schema import UpdateTransactionSchema
from db import get_db
from sqlalchemy.orm import Session
from models import Transaction,User
from fastapi import APIRouter,HTTPException,Depends


router = APIRouter(prefix="/transactions")
@router.put("/")
def updatestatus(data:UpdateTransactionSchema,db:Session=Depends(get_db)):
    existing = db.query(Transaction).filter(Transaction.id == data.transaction_id).first()
    if not existing:
        raise HTTPException(status_code=404,detail="the id is invalid")
    existing.amount = data.amount
    existing.type = data.type
    existing.category = data.category
    existing.note = data.note
    existing.date = data.date
    db.commit()
    db.refresh(existing)

    return {
        "message": "Transaction updated"
    }