from fastapi import FastAPI

from app.api.routes.health import router as health_router


app = FastAPI(
    title="ALPIP API",
    description="Arabic Legal Intelligence Platform API",
    version="0.1.0"
)


app.include_router(
    health_router,
    prefix="/api"
)


@app.get("/")
def root():
    return {
        "name": "ALPIP",
        "status": "running"
    }
