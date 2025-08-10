from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.models.citys import City
from app.repositories.citys import city_repositories
from app.schemas.citys import CityCread, CityDB, CityRead

city = APIRouter()

@city.post("/citys", response_model=CityDB)
async def create_city(
    name_city: str, session: AsyncSession = Depends(get_async_session)
) -> CityDB:
    new_city = await city_repositories.creat(
        name_city=name_city, session=session
    )
    return new_city
