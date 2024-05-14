from pydantic import BaseModel, EmailStr
from typing import List, Optional

# Schema for incoming data
class ResumeCreate(BaseModel):
    name: str
    email: EmailStr
    template: str

# Schema for outgoing data, including the ID and potentially other fields you want to expose
class ResumeResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    template: str