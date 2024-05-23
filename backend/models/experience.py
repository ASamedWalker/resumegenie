from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import JSON, Column
from typing import List, Optional

class Experience(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    resume_id: int = Field(default=None, foreign_key="resume.id")
    position: str
    company: str
    location: str
    start_date: str
    end_date: str
    duties: Optional[List[str]] = Field(sa_column=Column(JSON), default=[])
    resume: "Resume" = Relationship(back_populates="experiences")
