from pydantic_settings import BaseSettings
from pydantic import BaseModel


class RunConfig(BaseModel):  # BaseModel задает структуру данных
    host: str = "0.0.0.0"
    port: int = 8000


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class Settings(BaseSettings):  # BaseSettings задает основные настройки, ну также может там из файликов брать .env данные
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()


settings = Settings()