from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.citys import City
from app.repositories.storage import Repositories


class CityRepositories(Repositories):
    """Операции с городами."""

    def __init__(self, model):
        self.model = model

    async def get_by_id(self, pk: int, session: AsyncSession) -> City:
        """Получает город по его ID.
        Аргументы:
            pk (int): Первичный ключ (ID) города.
            session (AsyncSession): Сессия SQLAlchemy для работы с БД.
        """
        obj = await session.execute(
            select(self.model).where(self.model.id == pk)
        )
        return obj.scalar()

    async def get_by_name(self, name: str, session: AsyncSession) -> City:
        """Получает город по его названию.
        Аргументы:
            name (str): Название города.
            session (AsyncSession): Сессия SQLAlchemy для работы с БД.
        """
        obj = await session.execute(
            select(self.model).where(self.model.city_name == name)
        )
        return obj.scalar()

    async def get_multy(self, session: AsyncSession) -> list[City]:
        """Получает список всех городов.
        Аргументы:
            session (AsyncSession): Сессия SQLAlchemy для работы с БД.
        """
        objects = await session.execute(select(self.model))
        return objects.scalars().all()

    async def creat(self, name_city: int, session: AsyncSession) -> City:
        """Создает новый город.
        Аргументы:
            name_city (str): Название нового города.
            session (AsyncSession): Сессия SQLAlchemy для работы с БД.
        """
        new_city = City(city_name=name_city)
        session.add(new_city)
        await session.commit()
        return new_city

    async def delete(self, obj: City, session: AsyncSession) -> None:
        """Удаляет город.
        Аргументы:
            obj (City): Объект города, который нужно удалить.
            session (AsyncSession): Сессия SQLAlchemy для работы с БД.
        """
        await session.delete(obj)
        await session.commit()


city_repositories = CityRepositories(City)
