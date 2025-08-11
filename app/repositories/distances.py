from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.distances import Distance
from app.repositories.storage import Repositories


class DistanceRepositories(Repositories):
    """Операции с моделью Wallet."""

    def __init__(self, model):
        self.model = model

    async def get_by_id(self, pk: int, session: AsyncSession) -> Distance:
        """Получает расстояние по его ID.
        Аргументы:
            pk (int): Первичный ключ (ID) записи расстояния.
            session (AsyncSession): Асинхронная сессия SQLAlchemy.
        """
        obj = await session.execute(
            select(self.model).where(self.model.id == pk)
        )
        return obj.scalar()

    async def get_distance_with_citys(
        self, city_from: str, city_to: str, session: AsyncSession
    ) -> Distance:
        """Получает расстояние между двумя городами по их названиям.
        Аргументы:
            city_from (str): Название города отправления.
            city_to (str): Название города назначения.
            session (AsyncSession): Асинхронная сессия SQLAlchemy.
        """
        obj = await session.execute(
            select(self.model).where(
                and_(
                    self.model.city_from == city_from,
                    self.model.city_to == city_to,
                )
            )
        )
        return obj.scalar()

    async def get_multy(self, session: AsyncSession) -> list[Distance]:
        """Получает список всех расстояний.
        Аргументы:
            session (AsyncSession): Асинхронная сессия SQLAlchemy.
        """
        objects = await session.execute(select(self.model))
        return objects.scalars().all()

    async def creat(
        self,
        name_city_from: str,
        name_city_to: str,
        distance: int,
        session: AsyncSession,
    ) -> Distance:
        """Создает новое расстояние между городами.
        Аргументы:
            name_city_from (str): Название города отправления.
            name_city_to (str): Название города назначения.
            distance (int): Расстояние в километрах.
            session (AsyncSession): Асинхронная сессия SQLAlchemy.
        """
        new_distance = Distance(
            city_from=name_city_from, city_to=name_city_to, distance=distance
        )
        session.add(new_distance)
        await session.commit()
        return new_distance

    async def delete(self, obj: Distance, session: AsyncSession) -> None:
        """Удаляет расстояние между городами.
        Аргументы:
            obj (Distance): Объект Distance, который нужно удалить.
            session (AsyncSession): Асинхронная сессия SQLAlchemy.
        """
        await session.delete(obj)
        await session.commit()


distance_repositories = DistanceRepositories(Distance)
