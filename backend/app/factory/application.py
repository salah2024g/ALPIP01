from backend.app.api.router import api_router
from backend.app.config.settings import settings
from fastapi import FastAPI


def create_application():

    app = FastAPI(title=settings.app_name, version=settings.version)

    app.include_router(api_router)

    return app
