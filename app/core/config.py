from pathlib import Path


class Settings:
    """Настройки приложения."""

    BASE_DIR: str = Path(__file__).resolve().parent.parent


    @property
    def base_dir(self):
        return self.BASE_DIR



setting = Settings()