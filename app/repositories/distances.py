from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.distances import Distance
from app.repositories.storage import Repositories


class DistanceRepositories(Repositories):
    """Операции с моделью Wallet."""

    def __init__(self, model):
        self.model = model

    async def get_by_id(self, pk: int, session: AsyncSession) -> Distance:
        """Получаем объект по id."""
        obj = await session.execute(
            select(self.model).where(self.model.id == pk)
        )
        return obj.scalar()

    async def get_multy(self, session: AsyncSession) -> list[Distance]:
        """Получаем несколько объектов."""
        objects = await session.execute(select(self.model))
        return objects.scalars().all()


distance_repositories = DistanceRepositories(Distance)
