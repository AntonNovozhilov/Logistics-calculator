from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.v1.index import router
from app.core.config import setting

app = FastAPI()

app.mount("/static", StaticFiles(directory=setting.BASE_DIR / "static"), name="static")

app.include_router(router)
