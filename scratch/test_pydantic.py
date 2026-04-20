from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class TestModel(BaseModel):
    d: Optional[date] = Field(default_factory=date.today)

print(TestModel().d)
