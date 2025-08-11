from pydantic import BaseModel, Field


class DistanceBase(BaseModel):
    """Базовая схема для расстояний."""

    city_from: str = Field(...)
    city_to: str = Field(...)
    distance: int = Field(..., gt=0)


class DistanceRead(DistanceBase):
    """Схема для расстояний."""


class DistanceCread(DistanceBase):
    """Схема для создания расстояний."""


class DistanceDB(DistanceBase):
    """Схема для расстояний из БД."""

    id: int

    class Config:
        orm_mode = True
