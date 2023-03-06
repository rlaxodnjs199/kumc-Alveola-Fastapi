from datetime import date
from typing import Optional

from pydantic import BaseModel


class SubjectBase(BaseModel):
    subj: str
    description: Optional[str]

    class Config:
        orm_mode = True


class SubjectCreate(SubjectBase):
    study_id: str
    mrn: str
    birth_date: Optional[date]
    height: Optional[float]
    weight: Optional[float]
    gender: Optional[bool]
    project_id: int


class SubjectRead(SubjectBase):
    pass


class SubjectUpdate(BaseModel):
    pass
