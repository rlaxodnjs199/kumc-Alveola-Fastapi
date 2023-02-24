from typing import Optional
from pydantic import BaseModel, Field


class ProjectBaseSchema(BaseModel):
    name: str


class ProjectCreate(ProjectBaseSchema):
    description: Optional[str] = Field(None, nullable=True)


class ProjectUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
