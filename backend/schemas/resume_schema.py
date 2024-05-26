from pydantic import BaseModel, EmailStr, validator
from typing import List, Optional
from enum import Enum
from .education_schema import EducationRead
from .skill_schema import SkillRead
from .project_schema import ProjectRead
from .experience_schema import ExperienceRead
from .certification_schema import CertificationRead


class TemplateName(str, Enum):
    modern = "Modern"
    traditional = "Traditional"
    creative = "Creative"


class ResumeBase(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str] = None  # Optionally include phone
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    website: Optional[str] = None
    template: TemplateName = TemplateName.modern

    @validator("name")
    def validate_name(cls, value):
        if not value:
            raise ValueError("Name must not be empty")
        return value


class ResumeCreate(ResumeBase):
    pass


class ResumeRead(ResumeBase):
    id: int


class ResumeUpdate(ResumeBase):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone: Optional[str] = None
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    website: Optional[str] = None
    template: Optional[TemplateName] = None
    # Consider how you'd want to handle updates to nested objects, potentially as separate actions/APIs
