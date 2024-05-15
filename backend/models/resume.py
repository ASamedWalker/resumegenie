from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship
from pydantic import EmailStr

class Resume(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100, index=True)
    email: str = Field(max_length=100, index=True)
    template: str
    education_details: List["Education"] = Relationship(back_populates="resume")
    skills: List["Skill"] = Relationship(back_populates="resume")
    projects: List["Project"] = Relationship(back_populates="resume")
