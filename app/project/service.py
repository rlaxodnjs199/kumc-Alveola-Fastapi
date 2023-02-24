from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert, update, delete

from .models import Project
from .schemas import ProjectCreate, ProjectUpdate


class ProjectService:
    @staticmethod
    async def get_project(
        *, db_session: AsyncSession, project_id: int
    ) -> Optional[Project]:
        """Returns a project based on the project_id"""
        project = await db_session.get(Project, project_id)
        await db_session.commit()
        return project

    @staticmethod
    async def create_project(
        *, db_session: AsyncSession, project_in: ProjectCreate
    ) -> Optional[Project]:
        """Creates a project"""
        stmt = insert(Project).values(**project_in.dict())
        project = await db_session.execute(stmt)
        await db_session.commit()
        return project

    @staticmethod
    async def update_project(
        *, db_session: AsyncSession, project_id: int, project_in: ProjectUpdate
    ) -> Optional[Project]:
        """Updateds a project"""
        stmt = (
            update(Project).where(Project.id == project_id).values(**project_in.dict())
        )
        project = await db_session.execute(stmt)
        await db_session.commit()
        return project

    @staticmethod
    async def delete_project(*, db_session: AsyncSession, project_id: int):
        """Deletes a project"""
        stmt = delete(Project).where(Project.id == project_id)
        await db_session.execute(stmt)
        await db_session.commit()
