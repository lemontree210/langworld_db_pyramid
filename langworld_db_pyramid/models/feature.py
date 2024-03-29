from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from langworld_db_pyramid.dbutils.query_mixin import QueryMixin
from langworld_db_pyramid.models.meta import Base


class Feature(QueryMixin, Base):  # type: ignore[misc]
    __tablename__ = "features"
    id = Column(Integer, primary_key=True)
    man_id = Column(String(10), index=True)
    category_id = Column(Integer, ForeignKey("feature_categories.id"))
    is_multiselect = Column(Boolean)
    name_en = Column(String(100))
    name_ru = Column(String(100))
    description_html_en = Column(Text)
    description_html_ru = Column(Text)

    category = relationship("FeatureCategory", back_populates="features")
    values = relationship("FeatureValue", back_populates="feature")
