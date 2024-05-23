from pydantic import BaseModel, EmailStr, validator
from typing import List, Optional

class ExperienceCreate(BaseModel):
    position: str
    company: str
    location: str
    start_date: str
    end_date: str
    duties: List[str]

class ExperienceRead(BaseModel):
    id: int
    position: str
    company: str
    location: str
    start_date: str
    end_date: str
    duties: List[str]

class ExperienceUpdate(BaseModel):
    position: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    duties: Optional[List[str]] = None
