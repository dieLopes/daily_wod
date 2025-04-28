from sqlalchemy import Integer, String, Enum
from app.models.base import Base
import enum
from pydantic import BaseModel
from enum import Enum as PyEnum
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class WodType(enum.Enum):
    FOR_TIME = "For Time"
    EMOM = "EMOM"
    TABATA = "Tabata"
    AMRAP = "AMRAP"

class Wod(Base):
    __tablename__ = "wods"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    type: Mapped[WodType] = mapped_column(Enum(WodType), nullable=False)
    time_cap: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)

class WodTypePy(PyEnum):
    FOR_TIME = "For Time"
    EMOM = "EMOM"
    TABATA = "Tabata"
    AMRAP = "AMRAP"

class WodBase(BaseModel):
    type: WodTypePy
    time_cap: int
    description: str

    class Config:
        orm_mode = True

class WodOut(WodBase):
    id: int