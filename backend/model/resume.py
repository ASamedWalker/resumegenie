from pydantic import BaseModel, Field
from typing import Optional

class Resume(BaseModel):
    id: Optional[int] = Field(None, description="The unique identifier for the resume")
    name: str
    email: str
    phone: str
    summary: str
