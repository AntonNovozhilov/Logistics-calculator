## Calc-Logist
##### Calc-Logist — это веб-приложение для расчёта логистических ставок между городами России. Проект использует FastAPI, SQLAlchemy (async), PostgreSQL и позволяет:

- хранить города и расстояния между ними в базе данных;

- рассчитывать цену перевозки с учётом веса груза, дополнительных точек, типа груза и региона;

- предоставлять веб-форму для расчёта с фронтенда;

- работать через REST API и HTML-форму.
_____
##### Технологии
- Python 3.11

- FastAPI

- SQLAlchemy (Async)

- PostgreSQL

- Jinja2 для шаблонов

- Docker + Docker Compose

- Poetry для управления зависимостями
_____
##### Установка
Клонируйте репозиторий

git clone <ваш репозиторий>\
cd calc-logis

Настройте .env\
Пример .env:

POSTGRES_SERVER=localhost\
POSTGRES_PORT=5432\
POSTGRES_DB=calc_logist\
POSTGRES_USER=postgres\
POSTGRES_PASSWORD=postgres


Запуск через Docker Compose

docker-compose up --build


Это автоматически:
- создаст и запустит контейнер PostgreSQL;

- применит миграции Alembic;

- инициализирует базу данных начальными городами и расстояниями;

- Запустит FastAPI на http://localhost:8000.
 _____

##### REST API

Города\
GET /city/ — получить список городов

GET /city/{id} — получить город по ID

POST /city/ — создать город (name_city в теле запроса)

DELETE /city/ — удалить город (через зависимость от id)

Расстояния\
GET /distance/ — получить список расстояний

GET /distance/{id} — получить расстояние по ID

POST /distance/ — создать расстояние (distance, name_city_from, name_city_to)

DELETE /distance/ — удалить расстояние

Расчёт стоимости\
POST / — расчёт с таргетом (город → город)

POST /notarget — расчёт без таргета (км + вес)