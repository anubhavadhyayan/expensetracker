import datetime
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class ExpenseBase(BaseModel):
    amount: float = Field(..., gt=0)
    description: Optional[str] = None
    category: Optional[str] = "General"
    date: Optional[datetime.date] = Field(default_factory=datetime.date.today)

class ExpenseCreate(ExpenseBase):
    pass

class ExpenseUpdate(BaseModel):
    amount: Optional[float] = Field(None, gt=0)
    description: Optional[str] = None
    category: Optional[str] = None
    date: Optional[datetime.date] = None

class Expense(ExpenseBase):
    id: UUID
    created_at: datetime.datetime

    class Config:
        from_attributes = True

