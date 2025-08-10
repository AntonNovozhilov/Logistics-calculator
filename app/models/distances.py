from sqlalchemy import Column, ForeignKey, Integer, String

from app.core.db import Base


class Distance(Base):
    city_from = Column(String, ForeignKey("citys.city_name"), nullable=False)
    city_to = Column(String, ForeignKey("citys.city_name"), nullable=False)
    distance = Column(Integer)
