from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.pgsql import Base


class Project(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]
