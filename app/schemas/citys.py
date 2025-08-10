from pydantic import BaseModel, Field


class CityBase(BaseModel):
    city_name: str = Field(...)


class CityRead(CityBase): ...


class CityCread(CityBase): ...


class CityDB(CityBase):
    id: int

    class Config:
        orm_mode = True
