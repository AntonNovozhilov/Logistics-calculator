from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.citys import city_repositories
from app.repositories.distances import distance_repositories


class Validators:

    async def exist_obj(self, obj):
        """Проверяет, что объект существует.
        Аргументы:
            obj: Объект, который нужно проверить.
        """
        if not obj:
            raise HTTPException(
                status_code=HTTPStatus.NOT_FOUND,
                detail="Передаваемого объекта не существует.",
            )
        return obj

    async def double_check_city(self, name: str, session: AsyncSession):
        """Проверяет, что города с таким названием ещё нет в базе.
        Аргументы:
            name (str): Название города.
            session (AsyncSession): Сессия SQLAlchemy для работы с БД.
        """
        exit_city = await city_repositories.get_by_name(
            name=name, session=session
        )
        if exit_city:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail="Город с таким названием уже существует в базе данных.",
            )

    async def double_check_distance(
        self, city_name_from: str, city_name_to: str, session: AsyncSession
    ):
        """Проверяет, что расстояние между городами ещё не сохранено в базе.
        Аргументы:
            city_name_from (str): Название города-отправления.
            city_name_to (str): Название города-прибытия.
            session (AsyncSession): Сессия SQLAlchemy для работы с БД.
        """
        distance = await distance_repositories.get_distance_with_citys(
            city_from=city_name_from, city_to=city_name_to, session=session
        )
        if distance:
            raise HTTPException(
                status_code=HTTPStatus.CONFLICT,
                detail="Расстояние между городами с такими названиями "
                "уже существует в базе данных.",
            )


validator = Validators()
