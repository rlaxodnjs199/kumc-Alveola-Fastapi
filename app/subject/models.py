from datetime import date
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.db.pgsql.base import Base


class Subject(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    subj: Mapped[str] = mapped_column(unique=True)
    study_id: Mapped[str]
    mrn: Mapped[str]
    birth_date: Mapped[Optional[date]]
    height: Mapped[Optional[float]]
    weight: Mapped[Optional[float]]
    gender: Mapped[Optional[bool]]
    description: Mapped[Optional[str]]
    project_id = mapped_column(ForeignKey("project.id"))
