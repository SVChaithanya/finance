from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from db import get_db
from models import Transaction, User

router = APIRouter(prefix="/summary")


@router.get("/")
def get_summary(user_id: str, db: Session = Depends(get_db)):

    # 🔹 check user exists
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # 🔹 total income
    total_income = db.query(func.sum(Transaction.amount))\
        .filter(
            Transaction.user_id == user_id,
            Transaction.type == "income"
        ).scalar() or 0

    # 🔹 total expense
    total_expense = db.query(func.sum(Transaction.amount))\
        .filter(
            Transaction.user_id == user_id,
            Transaction.type == "expense"
        ).scalar() or 0

    # 🔹 balance
    balance = total_income - total_expense

    # 🔹 category breakdown
    category_data = db.query(
        Transaction.category,
        func.sum(Transaction.amount)
    ).filter(Transaction.user_id == user_id)\
     .group_by(Transaction.category).all()

    category_breakdown = {
        category: amount for category, amount in category_data
    }

    # 🔹 monthly totals (PostgreSQL)
    monthly_data = db.query(
        func.to_char(Transaction.date, 'YYYY-MM'),
        func.sum(Transaction.amount)
    ).filter(Transaction.user_id == user_id)\
     .group_by(func.to_char(Transaction.date, 'YYYY-MM')).all()

    monthly_totals = {
        month: amount for month, amount in monthly_data
    }

    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": balance,
        "category_breakdown": category_breakdown,
        "monthly_totals": monthly_totals
    }