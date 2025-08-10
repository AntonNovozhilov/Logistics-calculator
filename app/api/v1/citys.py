from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.models.citys import City
from app.repositories.citys import city_repositories
from app.schemas.citys import CityCread, CityDB, CityRead

city = APIRouter()


@city.get("/", response_model=list[CityDB], summary="Получить города из БД.")
async def get_all_citys(
    session: AsyncSession = Depends(get_async_session),
) -> list[CityDB]:
    """Получить города из БД."""
    result = await city_repositories.get_multy(session=session)
    return result


@city.get("/{pk}", response_model=CityDB, summary="Получить город БД.")
async def get_city(
    pk: int, session: AsyncSession = Depends(get_async_session)
) -> CityDB:
    """Получить город БД."""
    result = await city_repositories.get_by_id(pk=pk, session=session)
    return result


@city.post("/", response_model=CityDB, summary="Создать город в БД.")
async def create_city(
    name_city: str, session: AsyncSession = Depends(get_async_session)
) -> CityDB:
    """Создать город в БД."""
    new_city = await city_repositories.creat(
        name_city=name_city, session=session
    )
    return new_city


@city.delete("/", response_model=CityDB, summary="Удалить город из БД.")
async def delete_city(
    city_obj: City = Depends(get_city),
    session: AsyncSession = Depends(get_async_session),
) -> CityDB:
    """Удалить город из БД."""
    await city_repositories.delete(obj=city_obj, session=session)
    return city_obj
