from fastapi import FastAPI

from app.project.endpoints import router as project_router


def init_routers(app: FastAPI):
    app.include_router(project_router)
