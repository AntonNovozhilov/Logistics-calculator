from pydantic import BaseModel, Field


class CityBase(BaseModel):
    """Базовая схема городов."""

    city_name: str = Field(...)


class CityRead(CityBase):
    """Схема городов."""


class CityCread(CityBase):
    """Схема городов для создания."""


class CityDB(CityBase):
    """Схема городов для вывода инф с БД."""

    id: int

    class Config:
        orm_mode = True
