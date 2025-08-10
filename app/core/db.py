from typing import AsyncGenerator

from sqlalchemy import Column, Integer
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base, declared_attr

from app.core.config import setting


class PreBase:

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + "s"

    id = Column(Integer, primary_key=True, autoincrement=True)


Base = declarative_base(cls=PreBase)

engine = create_async_engine(url=setting.date_base)

AsyncSession = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator:
    async with AsyncSession() as session:
        yield session
