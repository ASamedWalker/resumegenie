from sqlmodel import SQLModel, Field


class Base(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)

    class Config:
        from_attributes = True
        arbitrary_types_allowed = True
