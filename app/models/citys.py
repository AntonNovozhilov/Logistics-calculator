from sqlalchemy import Column, String

from app.core.db import Base


class City(Base):
    city_name = Column(String, nullable=False, unique=True)
