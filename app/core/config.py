from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    """Настройки приложения."""

    BASE_DIR: Path = Path(__file__).resolve().parent.parent
    POSTGRES_PORT: int
    POSTGRES_SERVER: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    AVERAGE_DAY_KM: int = 800
    LEASING: int = 1_150_000
    DAYMONTH: int = 30
    WEIGTH_TRUCK: int = 20_000

    @property
    def date_base(self):
        """Путь к базе данных."""
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_SERVER}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    class Config:
        env_file = Path(__file__).resolve().parent.parent / ".env"


setting = Settings()
