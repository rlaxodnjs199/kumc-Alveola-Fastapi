from fastapi import FastAPI

from app.api import init_routers


def create_app() -> FastAPI:
    app = FastAPI(
        title="Alveola",
        description="Alveola Backend FastAPI",
        version="1.0.0",
    )
    init_routers(app)

    return app


app = create_app()
