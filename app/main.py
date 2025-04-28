from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.config.database import engine
from app.models.base import Base
from app.utils.seed_admin import seed_admin
from app.routes.wod_routes import wod_router
from app.routes.auth_routes import auth_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    seed_admin()
    yield

app = FastAPI(
    lifespan=lifespan,
    title="API de Treinos de Crossfit",
    description="Esta API permite consulta de treinos de crossfit",
    version="1.0.0"
)

app.include_router(wod_router)
app.include_router(auth_router)