from fastapi import FastAPI
from .expenses.router import router as expense_router

app = FastAPI(title="Expense Tracker API", description="FastAPI + Supabase Expense Tracker")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Expense Tracker API!"}

# Include routers
app.include_router(expense_router)
