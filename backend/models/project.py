from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional


class Project(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    resume_id: int =Field(default=None, foreign_key="resume.id")
    name: str = Field(max_length=100, index=True)
    description: str
    url: str
    start_date: str
    end_date: str
    resume: "Resume" = Relationship(back_populates="projects")