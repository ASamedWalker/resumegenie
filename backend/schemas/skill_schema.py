from pydantic import BaseModel, Field
from typing import List, Optional

class SkillCreate(BaseModel):
    name: str
    level: str  # Assuming 'level' is a descriptive field like 'Beginner', 'Intermediate', 'Expert'
    resume_id: int

class SkillRead(BaseModel):
    id: int
    name: str
    level: str

class SkillUpdate(BaseModel):
    name: Optional[str] = None
    level: Optional[str] = None