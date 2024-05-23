from sqlmodel import Field, SQLModel, Relationship
from typing import List, Optional

class Certification(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    resume_id: int = Field(default=None, foreign_key="resume.id")
    title: str
    description: Optional[str] = None  # Description of the honor or certification
    issuing_organization: Optional[str] = None  # For certifications, primarily
    date_received: Optional[str] = None  # Date the honor or certification was received
    resume: "Resume" = Relationship(back_populates="certifications")