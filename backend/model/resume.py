from pydantic import BaseModel

class Resume(BaseModel):
    name: str
    email: str
    phone: str
    summary: str
