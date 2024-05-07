from datetime import date
from sqlmodel import SQLModel, Field, Relationship
from .base import Base

class Certifications(Base, table=True):
    id: int = Field(default=None, primary_key=True)
    resume_id: int = Field(foreign_key="resume.id")
    name: str
    issued_by: str
    date_issued: date

    resume: "Resume" = Relationship(back_populates="certifications")
