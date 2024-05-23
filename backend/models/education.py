from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional

class Education(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    resume_id: int = Field(default=None, foreign_key="resume.id")
    school: str = Field(max_length=100, index=True)
    degree: str = Field(max_length=100)
    major: str = Field(max_length=100)
    start_date: str
    end_date: str
    resume: Optional["Resume"] = Relationship(back_populates="education")