from typing import List
from typing import Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import SubjectCreate
from .schemas import SubjectRead
from .service import SubjectService
from app.db.pgsql.session import get_db

router = APIRouter(
    prefix="/api/subjects",
    tags=["subject"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[Optional[SubjectRead]])
async def get_all_subjects(*, db_session: AsyncSession = Depends(get_db)):
    """Get all subjects"""
    subjects = await SubjectService.get_all_subjects(db_session=db_session)
    return subjects


@router.get("/{subject_id}", response_model=SubjectRead)
async def get_subject(
    *, db_session: AsyncSession = Depends(get_db), subject_id: int
):
    subject = await SubjectService.get_subject(
        db_session=db_session, subject_id=subject_id
    )
    if not subject:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "Subject does not exist."}],
        )
    return subject


@router.post("")
async def create_subject(
    *, db_session: AsyncSession = Depends(get_db), subject_in: SubjectCreate
):
    """Create a new subject"""
    await SubjectService.create_subject(
        db_session=db_session, subject_in=subject_in
    )
