from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from langworld_db_pyramid.models.meta import Base


class FeatureCategory(Base):  # type: ignore[misc]
    __tablename__ = "feature_categories"
    id = Column(Integer, primary_key=True)
    man_id = Column(String(2), index=True)
    name_en = Column(String(100))
    name_ru = Column(String(100))
    features = relationship("Feature", back_populates="category")
