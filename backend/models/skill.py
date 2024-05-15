from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional


class Skill(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    resume_id: int = Field(foreign_key="resume.id")
    name: str = Field(max_length=100, index=True)
    level: str
    resume: "Resume" = Relationship(back_populates="skills")
