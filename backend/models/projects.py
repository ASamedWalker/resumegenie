from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship
from datetime import  date
from .base import Base

class Projects(Base, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    resume_id: int = Field(foreign_key="resume.id")
    project_name: str = Field(max_length=100)
    project_description: str = Field(max_length=1000)
    start_date: Optional[str] = date
    end_date: Optional[str] = date
    project_link: Optional[str] = None
    resume: List["Resume"]= Relationship(back_populates="project_details")