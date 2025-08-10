import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.v1.index import router
from app.api.v1.citys import city
from app.core.config import setting

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=setting.BASE_DIR / "static"),
    name="static",
)

app.include_router(router)
app.include_router(city)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
