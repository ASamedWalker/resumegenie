from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional
from datetime import datetime, date
from .base import Base


class User(Base, table=True):
    id: int = Field(default=None, primary_key=True)
    username: str = Field(max_length=50, unique=True, index=True)
    email: str = Field(max_length=100, unique=True, index=True)
    password_hash: str = Field(max_length=100)
    resume: List["Resume"] = Relationship(back_populates="user")
