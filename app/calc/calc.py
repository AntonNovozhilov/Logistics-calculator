from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import setting
from app.repositories.distances import distance_repositories
from app.validators.validators import validator


class CalculatorTarget:
    def __init__(
        self,
        city_from: str,
        city_to: str,
        weight: int,
        extra_points: int,
        from_region: bool,
        to_region: bool,
        cargo_easy: bool,
        cargo_hard: bool,
        dfo: bool,
        session: AsyncSession,
        average_daily_km: int = setting.AVERAGE_DAY_KM,
    ):
        self.city_from = city_from
        self.city_to = city_to
        self.weight = weight
        self.extra_points = extra_points
        self.from_region = from_region
        self.to_region = to_region
        self.cargo_easy = cargo_easy
        self.cargo_hard = cargo_hard
        self.dfo = dfo
        self.session = session
        self.average_daily_km = average_daily_km
        self.leasing_per_month = setting.LEASING
        self.days_per_month = setting.DAYMONTH
        self.weight_truck = setting.WEIGTH_TRUCK

    async def _get_distance(self) -> float:
        """Получаем расстояние между городами, учитывая область."""
        distance_obj = await distance_repositories.get_distance_with_citys(
            city_from=self.city_from,
            city_to=self.city_to,
            session=self.session,
        )
        await validator.exist_obj(distance_obj)

        distance = distance_obj.distance
        if self.from_region:
            distance += 350
        if self.to_region:
            distance += 350
        return distance

    def _calculate_base_price(self, days: float) -> float:
        """Базовая ставка — дневная ставка * количество дней."""
        daily_leasing = self.leasing_per_month / self.days_per_month
        return daily_leasing * days

    def _apply_weight_adjustment(self, price: float) -> float:
        """Корректируем цену в зависимости от веса."""
        if self.weight > self.weight_truck:
            tons_over = (self.weight - self.weight_truck) / 1000
            price *= 1 + 0.01 * tons_over
        return price

    def _apply_extra_points(self, price: float) -> float:
        """Добавляем стоимость за дополнительные точки."""
        if self.extra_points > 0:
            price += self.extra_points * 10_000
        return price

    def _apply_cargo_type_adjustment(self, price: float) -> float:
        """Применяем корректировки по типу груза."""
        if self.cargo_easy:
            price *= 0.85
        if self.cargo_hard:
            price *= 1.20
        return price

    def _apply_dfo_adjustment(self, price: float) -> float:
        """Добавляем наценку для ДФО."""
        if self.dfo:
            price += 20_000
        return price

    async def calculate_price(self) -> int:
        """Главный метод — вычислить итоговую ставку."""
        distance = await self._get_distance()
        days = distance / self.average_daily_km
        price = self._calculate_base_price(days)
        price = self._apply_weight_adjustment(price)
        price = self._apply_extra_points(price)
        price = self._apply_cargo_type_adjustment(price)
        price = self._apply_dfo_adjustment(price)
        return int(price)


class CalculatorNoTarget:

    def __init__(
        self,
        km: int,
        weight: int,
    ):
        self.km = km
        self.weight = weight

    def calculate_price(self) -> int:
        price = self.km * 75
        if self.weight > setting.WEIGTH_TRUCK:
            over_tons = (self.weight - setting.WEIGTH_TRUCK) / 1000
            price *= 1 + 0.01 * over_tons
        return price
