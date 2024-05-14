from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship
from datetime import date


class EducationDetail(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    resume_id: int = Field(foreign_key="resume.id")
    institution_name: str = Field(max_length=100)
    degree: str = Field(max_length=50)
    start_date: Optional[str] = date
    end_date: Optional[str] = date
    description: Optional[str] = None
    resume: "Resume" = Relationship(back_populates="education_details")