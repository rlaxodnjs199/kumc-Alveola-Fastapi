from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.pgsql.session import get_db
from .service import ProjectService
from .schemas import ProjectCreate, ProjectUpdate

router = APIRouter(
    prefix="/api/projects",
    tags=["project"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{project_id}")
async def get_project(*, db_session: AsyncSession = Depends(get_db), project_id: int):
    return await ProjectService.get_project(
        db_session=db_session, project_id=project_id
    )


@router.post("/")
async def create_project(
    *, db_session: AsyncSession = Depends(get_db), project_in: ProjectCreate
):
    """Create a new project."""
    project = await ProjectService.create_project(
        db_session=db_session, project_in=project_in
    )
    return project


@router.put("/")
async def update_project(
    *,
    db_session: AsyncSession = Depends(get_db),
    project_id: int,
    project_in: ProjectUpdate
):
    """
    ToDo
    1. Make it work without typing name by merge default project from project_id and project_in
    2. Error handling
    3. Return type processing
    """
    project = await ProjectService.update_project(
        db_session=db_session, project_id=project_id, project_in=project_in
    )
    return project


@router.delete("/{project_id}")
async def delete_project(
    *, db_session: AsyncSession = Depends(get_db), project_id: int
):
    await ProjectService.delete_project(db_session=db_session, project_id=project_id)
    return
