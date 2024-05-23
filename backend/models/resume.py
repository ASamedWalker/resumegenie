from typing import List, Optional
from sqlmodel import Field, SQLModel, Relationship
from pydantic import EmailStr


class Resume(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100, index=True)
    email: str = Field(max_length=100, index=True)
    phone: Optional[str] = Field(default=None)
    linkedin_url: Optional[str] = Field(default=None)  # Optional LinkedIn URL
    github_url: Optional[str] = Field(default=None)  # Optional GitHub URL
    website: Optional[str] = Field(default=None)  # Optional personal website
    template: str
    education: List["Education"] = Relationship(back_populates="resume")
    skills: List["Skill"] = Relationship(back_populates="resume")
    projects: List["Project"] = Relationship(back_populates="resume")
    experiences: List["Experience"] = Relationship(back_populates="resume")
    certifications: List["Certification"] = Relationship(back_populates="resume")
