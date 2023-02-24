from sqlalchemy import Column, DateTime, func
from sqlalchemy.orm import as_declarative, declared_attr


@as_declarative()
class Base:
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
