from pydantic import BaseModel, Field
from typing import List, Optional


class TemplateCreate(BaseModel):
    name: str
    content: str = Field(default="")
    description: str


class TemplateRead(BaseModel):
    id: int
    name: str
    content: str
    description: str


class TemplateUpdate(BaseModel):
    name: Optional[str] = None
    content: Optional[str] = None
    description: Optional[str] = None
