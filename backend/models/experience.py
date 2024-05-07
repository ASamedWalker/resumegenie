from datetime import date
from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship
from .base import Base


class ExperienceDetail(Base, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    resume_id: int = Field(foreign_key="resume.id")
    company_name: str = Field(max_length=100)
    role: str = Field(max_length=50)
    start_date: Optional[str] = date
    end_date: Optional[str] = date
    description: Optional[str] = None

    resume: "Resume" = Relationship(back_populates="experience_details")