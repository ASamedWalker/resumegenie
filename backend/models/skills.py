from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship


class Skill(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    resume_id: int = Field(foreign_key="resume.id")
    name: str = Field(max_length=100)
    proficiency_level: str = Field(max_length=100)
    resume: "Resume" = Relationship(back_populates="skills")
