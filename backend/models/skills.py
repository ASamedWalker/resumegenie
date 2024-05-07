from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship
from .base import Base


class Skills(Base, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    resume_id: int = Field(foreign_key="resume.id")
    name: str = Field(max_length=100)
    proficiency_level: str = Field(max_length=100)

    resume: List["Resume"] = Relationship(back_populates="skills")
