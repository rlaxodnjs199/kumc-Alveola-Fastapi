from typing import List
from typing import Optional

from pydantic import BaseModel

from app.subject.schemas import SubjectRead


class ProjectBase(BaseModel):
    name: str
    description: Optional[str]

    class Config:
        orm_mode = True


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    id: Optional[int]
    name: Optional[str]
    description: Optional[str]

    class Config:
        orm_mode = True


class ProjectRead(ProjectBase):
    subjects: List[Optional[SubjectRead]]
