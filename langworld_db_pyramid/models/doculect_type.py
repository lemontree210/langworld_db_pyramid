from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from langworld_db_pyramid.models.meta import Base


class DoculectType(Base):  # type: ignore[misc]
    __tablename__ = "doculect_types"
    id = Column(Integer, primary_key=True)
    name_en = Column(String(50))
    name_ru = Column(String(50))
    doculects = relationship("Doculect", back_populates="type")
