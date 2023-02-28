from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker

from app.config import config


engine = create_async_engine(config.postgres_dsn, echo=True)
async_session_maker = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)


async def get_db() -> AsyncSession:
    async with async_session_maker() as session:
        yield session
