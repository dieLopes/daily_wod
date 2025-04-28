from sqlalchemy import Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship, Mapped, mapped_column
from app.models.base import Base
from app.models.wod import Wod

class DailyWod(Base):
    __tablename__ = "daily_wods"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    warm_up: Mapped[str] = mapped_column(String, nullable=False)
    skill: Mapped[str] = mapped_column(String, nullable=False)
    wod_id: Mapped[int] = mapped_column(Integer, ForeignKey("wods.id"), nullable=False)
    date: Mapped[str] = mapped_column(Date, nullable=False)

    wod: Mapped[Wod] = relationship("Wod", backref="daily_wods")