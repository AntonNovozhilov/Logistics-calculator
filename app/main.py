import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.v1.main_router import main_router
from app.core.config import setting

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=setting.BASE_DIR / "static"),
    name="static",
)

app.include_router(main_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
