from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.wod_service import get_all, get_by_id
from app.config.database import get_db
from app.models.wod import WodOut

wod_router = APIRouter()

@wod_router.get("/wods",
    response_model=list[WodOut],
    summary="Obter todos os treinos",
    description="Recupera todos os wods salvos na base de dados",
    response_description="Detalhes dos treinos",
    tags=["Wods"],)
def read_wods(db: Session = Depends(get_db)):
    wods = get_all(db)
    return wods

@wod_router.get("/wod/{wod_id}",
    response_model=WodOut,
    summary="Obtem o treino a partir do identificador",
    description="Recupera um treino da base de dados a partir do identificador",
    response_description="Detalhes dos treinos",
    tags=["Wods"],)
def read_wod(wod_id: int, db: Session = Depends(get_db)):
    wod = get_by_id(db, wod_id)
    if wod is None:
        raise HTTPException(status_code=404, detail="WOD not found")
    return wod
