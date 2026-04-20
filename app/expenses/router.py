from fastapi import APIRouter, HTTPException
from typing import List
from uuid import UUID
from . import crud, schemas

router = APIRouter(
    prefix="/expenses",
    tags=["expenses"]
)

@router.post("/create", response_model=schemas.Expense)
def create_expense(expense: schemas.ExpenseCreate):
    try:
        return crud.create_expense(expense)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=List[schemas.Expense])
def read_expenses():
    try:
        return crud.get_expenses()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{expense_id}", response_model=schemas.Expense)
def read_expense(expense_id: UUID):
    expense = crud.get_expense(expense_id)
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found")
    return expense

@router.put("/{expense_id}", response_model=schemas.Expense)
def update_expense(expense_id: UUID, expense: schemas.ExpenseUpdate):
    try:
        updated_expense = crud.update_expense(expense_id, expense)
        if updated_expense is None:
            raise HTTPException(status_code=404, detail="Expense not found")
        return updated_expense
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{expense_id}")

def delete_expense(expense_id: UUID):
    try:
        result = crud.delete_expense(expense_id)
        if not result:
            raise HTTPException(status_code=404, detail="Expense not found")
        return {"message": "Expense deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
