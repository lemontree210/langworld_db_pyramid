from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from langworld_db_pyramid.models.meta import Base


class Glottocode(Base):  # type: ignore[misc]
    __tablename__ = "glottocodes"
    id = Column(Integer, primary_key=True)
    code = Column(String(10), index=True)

    # Note that this is a many-to-many relationship. It is theoretically possible that not only one
    # doculect corresponds to many glottocodes, but one glottocode corresponds to many doculects.
    doculects = relationship(
        "Doculect", back_populates="glottocodes", secondary="doculect_to_glottocode"
    )
