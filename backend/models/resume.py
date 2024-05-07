from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship
from .base import Base



class Resume(Base, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    name: str = Field(max_length=100)
    email: str = Field(max_length=100)
    template: str = Field(max_length=50)
    user: "User" = Relationship(back_populates="resume")
    education_details: List["EducationDetail"] = Relationship(back_populates="resume")
    experience_details: List["ExperienceDetail"] = Relationship(back_populates="resume")
    skills: List["Skill"] = Relationship(back_populates="resume")
    certifications: List["Certification"] = Relationship(back_populates="resume")
    projects: List["Project"] = Relationship(back_populates="resume")
