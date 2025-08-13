from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    TELEGRAM_BOT_TOKEN: str
    YANDEX_API_KEY: str
    YANDEX_FOLDER_ID: str


    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
