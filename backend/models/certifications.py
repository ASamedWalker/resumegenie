from datetime import date
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class Certifications(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    resume_id: int = Field(foreign_key="resume.id")
    name: str
    issued_by: str
    date_issued: date

    resume: "Resume" = Relationship(back_populates="certifications")
