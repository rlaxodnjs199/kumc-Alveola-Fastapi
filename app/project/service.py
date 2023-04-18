from typing import List
from typing import Optional

from sqlalchemy import delete
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Project
from .schemas import ProjectCreate
from .schemas import ProjectUpdate


class ProjectService:
    @staticmethod
    async def get_all_projects(
        *, db_session: AsyncSession
    ) -> List[Optional[Project]]:
        q = await db_session.execute(select(Project))
        await db_session.commit()
        return q.scalars().all()

    @staticmethod
    async def get_project(
        *, db_session: AsyncSession, project_id: int
    ) -> Optional[Project]:
        project = await db_session.get(Project, project_id)
        await db_session.commit()
        return project

    @staticmethod
    async def get_project_by_name(
        *, db_session: AsyncSession, project_name: str
    ) -> Optional[Project]:
        q = await db_session.execute(
            select(Project).where(Project.name == project_name)
        )
        await db_session.commit()
        return q.one_or_none()

    @staticmethod
    async def create_project(
        *, db_session: AsyncSession, project_in: ProjectCreate
    ):
        stmt = insert(Project).values(**project_in.dict())
        await db_session.execute(stmt)
        await db_session.commit()

    @staticmethod
    async def update_project(
        *,
        db_session: AsyncSession,
        project: Project,
        project_in: ProjectUpdate,
    ):
        project_data = ProjectUpdate.from_orm(project).dict()
        to_update = {
            k: v for k, v in project_in.dict().items() if v is not None
        }
        project_data.update(to_update)

        stmt = (
            update(Project)
            .where(Project.id == project.id)
            .values(project_data)
        )
        await db_session.execute(stmt)
        await db_session.commit()

    @staticmethod
    async def delete_project(*, db_session: AsyncSession, project_id: int):
        stmt = delete(Project).where(Project.id == project_id)
        await db_session.execute(stmt)
        await db_session.commit()
