from typing import Optional
from sqlalchemy import Date, Float, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.db.pgsql.base import Base


class Subject(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    mrn: Mapped[str] = mapped_column(unique=True)
    birth_date: Mapped[Optional[Date]]
    height: Mapped[Optional[Float]]
    weight: Mapped[Optional[Float]]
    gender: Mapped[Optional[Boolean]]
    description: Mapped[Optional[str]]
