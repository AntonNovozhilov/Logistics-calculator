import pytest
from fastapi.testclient import TestClient

from app.calc.calc import CalculatorNoTarget
from app.core.db import get_async_session
from app.main import app
from app.models.citys import City
from app.models.distances import Distance

km = 100
weight = 1

km2 = 1000
weight2 = 25000


@pytest.fixture
def calc_t():
    calc = CalculatorNoTarget(km, weight)
    return calc


@pytest.fixture
def calc_t2():
    calc = CalculatorNoTarget(km2, weight2)
    return calc


city_samara = City(
    id=1,
    city_name="Самара",
)


city_moskow = City(
    id=2,
    city_name="Москва",
)


distace_sam_mos = Distance(
    id=1,
    city_from="Самара",
    city_to="Москва",
    distance=1075,
)


class FakeResult:
    def __init__(self, data):
        self.data = data

    def scalars(self):
        return self

    def all(self):
        return self.data

    def scalar(self):
        return self.data[0]


class FakeAsyncSession:
    async def execute(self, statement):
        if "citys" in str(statement):
            return FakeResult([city_samara, city_moskow])
        elif "distances" in str(statement):
            return FakeResult([distace_sam_mos])
        return FakeResult([])


@pytest.fixture
def fake_async_session():
    return FakeAsyncSession()


@pytest.fixture
def city_sam():
    return city_samara


@pytest.fixture
def city_mos():
    return city_moskow


@pytest.fixture
def dist_sam_mos():
    return distace_sam_mos


@pytest.fixture
def test_client(fake_async_session):
    def override_get_db():
        yield fake_async_session

    app.dependency_overrides[get_async_session] = override_get_db
    with TestClient(app) as client:
        yield client
