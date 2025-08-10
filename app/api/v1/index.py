from fastapi import APIRouter, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.core.config import setting

router = APIRouter()


router.mount(
    "/static",
    StaticFiles(directory=setting.BASE_DIR / "static"),
    name="static",
)

templates = Jinja2Templates(directory=setting.BASE_DIR / "templates")


@router.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "result": None}
    )


@router.post("/")
async def get_data_from_form(
    request: Request,
    distance: int = Form(),
    weight: int = Form(),
    dfo: bool = Form(default=False),
):
    price = distance * 65 + weight * 1500
    if dfo:
        price *= 1.5
    return templates.TemplateResponse(
        "index.html", {"request": request, "result": price}
    )
