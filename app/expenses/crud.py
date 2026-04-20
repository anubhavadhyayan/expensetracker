from ..database.database import supabase
from .schemas import ExpenseCreate, ExpenseUpdate


from uuid import UUID

def create_expense(expense: ExpenseCreate):
    # Convert Pydantic model to dict, making sure date is stringified for Supabase
    data = expense.model_dump()
    data['date'] = str(data['date'])
    response = supabase.table("expenses").insert(data).execute()
    return response.data[0]

def get_expenses():
    response = supabase.table("expenses").select("*").order("date", desc=True).execute()
    return response.data

def get_expense(expense_id: UUID):
    response = supabase.table("expenses").select("*").eq("id", str(expense_id)).execute()
    if response.data:
        return response.data[0]
    return None

def update_expense(expense_id: UUID, expense: ExpenseUpdate):
    data = expense.model_dump(exclude_unset=True)
    if 'date' in data and data['date']:
        data['date'] = str(data['date'])
    response = supabase.table("expenses").update(data).eq("id", str(expense_id)).execute()
    if response.data:
        return response.data[0]
    return None

def delete_expense(expense_id: UUID):
    response = supabase.table("expenses").delete().eq("id", str(expense_id)).execute()
    return response.data
