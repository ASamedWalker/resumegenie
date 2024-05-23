from pydantic import BaseModel, EmailStr, validator
from typing import List, Optional

class CertificationCreate(BaseModel):
    name: str
    issuing_organization: str
    date_received: str
    valid_until: Optional[str] = None

class CertificationRead(BaseModel):
    id: int
    name: str
    issuing_organization: str
    date_received: str
    valid_until: Optional[str]

class CertificationUpdate(BaseModel):
    name: Optional[str] = None
    issuing_organization: Optional[str] = None
    date_received: Optional[str] = None
    valid_until: Optional[str] = None
