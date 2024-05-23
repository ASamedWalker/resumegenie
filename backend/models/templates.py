from sqlmodel import SQLModel, Field


class Template(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str = Field(max_length=100)
    content: str
    description: str = Field(default="")  # Optional field
