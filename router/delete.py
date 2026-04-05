from db import get_db
from sqlalchemy.orm import Session
from models import Transaction
from fastapi import APIRouter,HTTPException,Depends


router = APIRouter(prefix="/delete")
@router.delete("/")
def Delete(transaction_id: str,db:Session=Depends(get_db)):
    existing = db.query(Transaction).filter(Transaction.id == transaction_id).first()
    if not existing:
        raise HTTPException(status_code=404,detail="the id is invalid that why we con't delete this data")
    db.delete(existing)
    db.commit()
    return{
        "status":"sucessfully deleted"
    }