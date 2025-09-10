from pydantic import BaseModel, Field
from typing import Optional


class Employee(BaseModel):
    id:int
    name:str = Field(..., min_length=3)
    department:Optional[str] = "General"
    salary=float = Field(..., ge=1000)