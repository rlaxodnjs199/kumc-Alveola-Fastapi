from typing import List
from typing import Optional

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import ProjectCreate
from .schemas import ProjectRead
from .schemas import ProjectUpdate
from .service import ProjectService
from app.db.pgsql.session import get_db

router = APIRouter(
    prefix="/api/projects",
    tags=["project"],
    responses={404: {"description": "Not found"}},
)


@router.get("", response_model=List[Optional[ProjectRead]])
async def get_all_projects(*, db_session: AsyncSession = Depends(get_db)):
    """Get all projects"""
    projects = await ProjectService.get_all_projects(db_session=db_session)
    return projects


@router.get("/{project_id}", response_model=ProjectRead)
async def get_project(
    *, db_session: AsyncSession = Depends(get_db), project_id: int
):
    """Get a project by the given id"""
    project = await ProjectService.get_project(
        db_session=db_session, project_id=project_id
    )
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "Project does not exist."}],
        )
    return project


@router.post("")
async def create_project(
    *, db_session: AsyncSession = Depends(get_db), project_in: ProjectCreate
):
    """Create a new project by the given name"""
    project = await ProjectService.get_project_by_name(
        db_session=db_session, project_name=project_in.name
    )
    if project:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=[{"msg": f"Project({project_in.name}) already exists"}],
        )
    await ProjectService.create_project(
        db_session=db_session, project_in=project_in
    )


@router.put("/{project_id}")
async def update_project(
    *,
    db_session: AsyncSession = Depends(get_db),
    project_id: int,
    project_in: ProjectUpdate,
):
    """Updates a project data with given data"""
    project = await ProjectService.get_project(
        db_session=db_session, project_id=project_id
    )
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "Project does not exist."}],
        )
    updated_project = await ProjectService.update_project(
        db_session=db_session, project=project, project_in=project_in
    )
    return updated_project


@router.delete("/{project_id}")
async def delete_project(
    *, db_session: AsyncSession = Depends(get_db), project_id: int
):
    """Delete a project by the given id"""
    project = await ProjectService.get_project(
        db_session=db_session, project_id=project_id
    )
    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=[{"msg": "Project does not exist."}],
        )
    await ProjectService.delete_project(
        db_session=db_session, project_id=project_id
    )
