from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.config.database import engine
from app.models.base import Base
from app.routes.wod_routes import wod_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(
    lifespan=lifespan,
    title="API de Treinos de Crossfit",
    description="Esta API permite consulta de treinos de crossfit",
    version="1.0.0"
)

app.include_router(wod_router)