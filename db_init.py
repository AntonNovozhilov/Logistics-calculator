import asyncio

from sqlalchemy import and_, select

from app.core.db import AsyncSession
from app.models.citys import City
from app.models.distances import Distance

russian_cities = [
    "Калининград",
    "Мурманск",
    "Санкт-Петербург",
    "Псков",
    "Великий Новгород",
    "Вологда",
    "Ярославль",
    "Архангельск",
    "Петрозаводск",
    "Москва",
    "Тверь",
    "Рязань",
    "Владимир",
    "Иваново",
    "Кострома",
    "Смоленск",
    "Калуга",
    "Тула",
    "Орёл",
    "Брянск",
    "Белгород",
    "Воронеж",
    "Липецк",
    "Курск",
    "Тамбов",
    "Саратов",
    "Волгоград",
    "Ростов-на-Дону",
    "Краснодар",
    "Ставрополь",
    "Астрахань",
    "Самара",
    "Тольятти",
    "Уфа",
    "Пермь",
    "Нижний Новгород",
    "Казань",
    "Ульяновск",
    "Челябинск",
    "Курган",
    "Тюмень",
    "Омск",
    "Новосибирск",
    "Кемерово",
    "Новокузнецк",
    "Барнаул",
    "Томск",
    "Красноярск",
    "Иркутск",
    "Улан-Удэ",
    "Чита",
    "Хабаровск",
    "Владивосток",
]

distance = [
    {"city_from": "Санкт-Петербург", "city_to": "Москва", "distance": 705},
    {"city_from": "Москва", "city_to": "Самара", "distance": 1075},
    {"city_from": "Самара", "city_to": "Челябинск", "distance": 987},
    {"city_from": "Челябинск", "city_to": "Новосибирск", "distance": 1563},
    {"city_from": "Новосибирск", "city_to": "Владивосток", "distance": 5645},
]


async def init_db():
    async with AsyncSession() as session:
        for city_name in russian_cities:
            city = await session.execute(
                select(City).where(City.city_name == city_name)
            )
            city = city.scalars().first()
            if not city:
                city = City(city_name=city_name)
                session.add(city)
                await session.commit()
                await session.refresh(city)
            else:
                continue
        for dist in distance:
            dist_obj = await session.execute(
                select(Distance).where(
                    and_(
                        Distance.city_from == dist["city_from"],
                        Distance.city_to == dist["city_to"],
                    )
                )
            )
            dist_obj = dist_obj.scalar()
            if not dist_obj:
                dist_obj = Distance(
                    city_from=dist["city_from"],
                    city_to=dist["city_to"],
                    distance=dist["distance"],
                )
                session.add(dist_obj)
                await session.commit()
                await session.refresh(dist_obj)
            else:
                continue


if __name__ == "__main__":
    asyncio.run(init_db())
