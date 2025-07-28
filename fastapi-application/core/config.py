from pydantic_settings import BaseSettings
from pydantic import BaseModel
from pydantic import PostgresDsn


class RunConfig(BaseModel):  # BaseModel задает структуру данных
    host: str = "0.0.0.0"
    port: int = 8000


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class DatabaseConfig(BaseSettings):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):  # BaseSettings задает основные настройки, ну также может там из файликов брать .env данные
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig = DatabaseConfig()


settings = Settings()