from pydantic import BaseModel, EmailStr, validator
from typing import List, Optional

class EducationCreate(BaseModel):
    school: str
    degree: str
    field_of_study: str
    start_date: str
    end_date: str

class EducationRead(BaseModel):
    id: int
    school: str
    degree: str
    field_of_study: str
    start_date: str
    end_date: str

class EducationUpdate(BaseModel):
    school: Optional[str] = None
    degree: Optional[str] = None
    field_of_study: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
