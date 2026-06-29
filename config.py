"""
AI Assistant Platform V2
config.py

Quản lý toàn bộ cấu hình hệ thống.

Không sử dụng os.getenv() ở bất kỳ nơi nào khác trong project.
Mọi cấu hình đều phải đi qua Settings().
"""

from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application Settings
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # ==========================================================
    # APP
    # ==========================================================

    APP_NAME: str = "AI Assistant Platform"

    APP_VERSION: str = "2.0.0"

    DEBUG: bool = False

    LOG_LEVEL: str = "INFO"

    # ==========================================================
    # TELEGRAM
    # ==========================================================

    BOT_TOKEN: str = Field(...)

    WEBHOOK_SECRET: str = Field(...)

    WEBHOOK_URL: str = Field(...)

    # ==========================================================
    # SUPABASE
    # ==========================================================

    SUPABASE_URL: str = Field(...)

    SUPABASE_KEY: str = Field(...)

    # ==========================================================
    # GEMINI
    # ==========================================================

    GEMINI_SECURE_1PSID: str = ""

    GEMINI_SECURE_1PSIDTS: str = ""

    # ==========================================================
    # IMAGE PROVIDERS
    # ==========================================================

    AI_HORDE_API_KEY: str = ""

    POLLINATIONS_API_KEY: str = ""

    # ==========================================================
    # CACHE
    # ==========================================================

    CACHE_TTL: int = 86400

    MAX_HISTORY: int = 20

    REQUEST_TIMEOUT: int = 60

    # ==========================================================
    # ADMIN
    # ==========================================================

    ADMIN_IDS: str = ""

    @property
    def admin_ids(self) -> list[int]:
        """
        ADMIN_IDS="123,456,789"

        ->

        [123,456,789]
        """

        if not self.ADMIN_IDS:

            return []

        return [
            int(x.strip())
            for x in self.ADMIN_IDS.split(",")
            if x.strip()
        ]


@lru_cache
def get_settings() -> Settings:
    """
    Singleton Settings
    """

    return Settings()


settings = get_settings()
