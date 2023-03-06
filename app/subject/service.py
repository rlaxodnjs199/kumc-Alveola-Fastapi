from typing import List
from typing import Optional

from sqlalchemy import delete
from sqlalchemy import insert
from sqlalchemy import select
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Subject
from .schemas import SubjectCreate
from .schemas import SubjectUpdate


class SubjectService:
    @staticmethod
    async def get_all_subjects(
        *, db_session: AsyncSession
    ) -> List[Optional[Subject]]:
        """Returns all subjects"""
        q = await db_session.execute(select(Subject))
        await db_session.commit()
        return q.scalars().all()

    @staticmethod
    async def get_subject(
        *, db_session: AsyncSession, subject_id: int
    ) -> Optional[Subject]:
        """Returns a subject with given id"""
        subject = await db_session.get(Subject, subject_id)
        await db_session.commit()
        return subject

    @staticmethod
    async def get_subject_by_name(
        *, db_session: AsyncSession, subject_name: str
    ) -> Optional[Subject]:
        """Returns a subject with the given subject_name"""
        q = await db_session.execute(
            select(Subject).where(Subject.subj == subject_name)
        )
        await db_session.commit()
        return q.one_or_none()

    @staticmethod
    async def create_subject(
        *, db_session: AsyncSession, subject_in: SubjectCreate
    ):
        """Creates a subject"""
        stmt = insert(Subject).values(**subject_in.dict())
        await db_session.execute(stmt)
        await db_session.commit()

    @staticmethod
    async def update_subject(
        *,
        db_session: AsyncSession,
        subject: Subject,
        subject_in: SubjectUpdate
    ):
        """Updateds a subject"""
        subject_data = SubjectUpdate.from_orm(subject).dict()
        to_update = {
            k: v for k, v in subject_in.dict().items() if v is not None
        }
        subject_data.update(to_update)

        stmt = (
            update(Subject)
            .where(Subject.id == subject.id)
            .values(subject_data)
        )
        await db_session.execute(stmt)
        await db_session.commit()

    @staticmethod
    async def delete_subject(*, db_session: AsyncSession, subject_id: int):
        """Deletes a subject"""
        stmt = delete(Subject).where(Subject.id == subject_id)
        await db_session.execute(stmt)
        await db_session.commit()
