from fastapi import FastAPI

from app.project.endpoints import router as project_router
from app.subject.endpoints import router as subject_router


def init_routers(app: FastAPI):
    app.include_router(project_router)
    app.include_router(subject_router)
