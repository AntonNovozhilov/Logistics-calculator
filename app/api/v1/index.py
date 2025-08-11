from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.ext.asyncio import AsyncSession

from app.calc.calc import CalculatorNoTarget, CalculatorTarget
from app.core.config import setting
from app.core.db import get_async_session

router = APIRouter()


def to_bool(val: str) -> bool:
    return val.lower() == "true"


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


@router.post("/", response_class=HTMLResponse)
async def calculate(
    request: Request,
    city_from: str = Form(...),
    city_to: str = Form(...),
    weight: int = Form(default=20000),
    extra_points: int = Form(default=0),
    from_region: str = Form(""),
    to_region: str = Form(""),
    cargo_easy: str = Form(""),
    cargo_hard: str = Form(""),
    dfo: str = Form(""),
    session: AsyncSession = Depends(get_async_session),
):
    calculator = CalculatorTarget(
        city_from=city_from,
        city_to=city_to,
        weight=weight,
        extra_points=extra_points,
        from_region=to_bool(from_region),
        to_region=to_bool(to_region),
        cargo_easy=to_bool(cargo_easy),
        cargo_hard=to_bool(cargo_hard),
        dfo=to_bool(dfo),
        session=session,
    )
    price = await calculator.calculate_price()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": price},
    )


@router.post("/notarget", response_class=HTMLResponse)
async def calculate_notarget(
    request: Request,
    km: int = Form(default=0),
    weight: int = Form(default=0),
):
    calculator = CalculatorNoTarget(km=km, weight=weight)
    price = calculator.calculate_price()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": price},
    )
