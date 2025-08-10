from sqlalchemy import Column, ForeignKey, Integer

from app.core.db import Base


class Distance(Base):
    city_from = Column(ForeignKey("citys.id"))
    city_to = Column(ForeignKey("citys.id"))
    distance = Column(Integer)
