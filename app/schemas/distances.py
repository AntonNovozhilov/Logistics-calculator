from pydantic import BaseModel, Field


class DistanceBase(BaseModel):
    city_from: str = Field(...)
    city_to: str = Field(...)
    distance: int = Field(..., gt=0)


class DistanceRead(DistanceBase): ...


class DistanceCread(DistanceBase): ...


class DistanceDB(DistanceBase):
    id: int

    class Config:
        orm_mode = True
