from pydantic import BaseModel, EmailStr, Field
from typing import Literal
from datetime import datetime

class RegisterSchema(BaseModel):
    name: str
    email: EmailStr
    password: str = Field(min_length=6)
    role: Literal['viewer', 'analyst', 'admin']


class LoginSchema(BaseModel):
    email: EmailStr
    password: str


class TransactionSchema(BaseModel):
    user_id: str
    amount: float = Field(gt=0)
    type: Literal['income', 'expense']
    category: str
    note: str | None = None
    date: datetime
    @validator('date')
    def date_must_be_past_or_today(cls, v):
        now = datetime.now()
        if v.date() > now.date():  # future day is not allowed
            raise ValueError("Date cannot be in the future")
        return v    
    


class UpdateTransactionSchema(BaseModel):
    transaction_id : str  
    amount: float = Field(gt=0)
    type: Literal['income', 'expense']
    category: str
    note: str | None = None
    date: datetime 
    @validator('date')
    def date_must_be_past_or_today(cls, v):
        now = datetime.now()
        if v.date() > now.date():  # future day is not allowed
            raise ValueError("Date cannot be in the future")
        return v

class delete(BaseModel):
    transaction_id : str
