from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.models.distances import Distance
from app.repositories.citys import city_repositories
from app.repositories.distances import distance_repositories
from app.schemas.distances import DistanceCread, DistanceDB, DistanceRead
from app.validators.validators import validator

distance = APIRouter()


@distance.get(
    "/",
    response_model=list[DistanceDB],
    summary="Получить расстояния между городами из БД.",
)
async def get_all_distances(
    session: AsyncSession = Depends(get_async_session),
) -> list[DistanceDB]:
    """Получить расстояния между городами из БД."""
    result = await distance_repositories.get_multy(session=session)
    return result


@distance.get(
    "/{pk}",
    response_model=DistanceDB,
    summary="Получить расстояние между городами из БД.",
)
async def get_distance(
    pk: int, session: AsyncSession = Depends(get_async_session)
) -> DistanceDB:
    """Получить расстояние между городами из БД."""
    result = await distance_repositories.get_by_id(pk=pk, session=session)
    await validator.exist_obj(obj=result)
    return result


@distance.post(
    "/",
    response_model=DistanceDB,
    summary="Создать расстояние между городами из БД.",
)
async def create_distance(
    distance: int,
    name_city_from: str,
    name_city_to: str,
    session: AsyncSession = Depends(get_async_session),
) -> DistanceDB:
    """Создать расстояние между городами из БД."""
    city_from = await city_repositories.get_by_name(
        name=name_city_from, session=session
    )
    city_to = await city_repositories.get_by_name(
        name=name_city_to, session=session
    )
    await validator.exist_obj(obj=city_from)
    await validator.exist_obj(obj=city_to)
    await validator.double_check_distance(
        city_name_from=city_from.city_name,
        city_name_to=city_to.city_name,
        session=session,
    )
    new_distance = await distance_repositories.creat(
        name_city_from=city_from.city_name,
        name_city_to=city_to.city_name,
        distance=distance,
        session=session,
    )
    return new_distance


@distance.delete(
    "/",
    response_model=DistanceDB,
    summary="Удалить расстояние между городами из БД.",
)
async def delete_distance(
    distance_obj: Distance = Depends(get_distance),
    session: AsyncSession = Depends(get_async_session),
) -> DistanceDB:
    """Удалить расстояние между городами из БД."""
    await validator.exist_obj(obj=distance_obj)
    await distance_repositories.delete(obj=distance_obj, session=session)
    return distance_obj
