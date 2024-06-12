from pydantic import BaseModel, EmailStr, validator
from typing import List, Optional

class CertificationCreate(BaseModel):
    title: str
    description: Optional[str] = None
    issuing_organization: str
    date_received: str


class CertificationRead(BaseModel):
    id: int



class CertificationUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    issuing_organization: Optional[str] = None
    date_received: Optional[str] = None