from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncSession


class Repositories(ABC):

    @abstractmethod
    async def get_by_id(self, pk: int, session: AsyncSession):
        """Получаем объект по id."""

    @abstractmethod
    async def get_multy(self, session: AsyncSession):
        """Получаем несколько объектов."""
