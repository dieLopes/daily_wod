from sqlalchemy.orm import Session
from app.models.wod import Wod

def get_all(db: Session):
    return db.query(Wod).all()

def get_by_id(db: Session, wod_id: int):
    return db.query(Wod).filter(Wod.id == wod_id).first()
