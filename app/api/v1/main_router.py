from fastapi import APIRouter

from app.api.v1.citys import city
from app.api.v1.distance import distance
from app.api.v1.index import router

main_router = APIRouter()
main_router.include_router(city, prefix="/city", tags=["Города"])
main_router.include_router(distance, prefix="/distance", tags=["Расстояния"])
main_router.include_router(router, tags=["Получение данных на фронте"])
