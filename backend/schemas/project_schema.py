from pydantic import BaseModel, EmailStr, validator
from typing import List, Optional

class ProjectCreate(BaseModel):
    name: str
    description: str
    url: str

class ProjectRead(BaseModel):
    id: int
    name: str
    description: str
    url: str

class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    url: Optional[str] = None
