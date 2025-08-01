from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from pydantic import PostgresDsn


class RunConfig(BaseModel):  # BaseModel задает структуру данных
    host: str = "0.0.0.0"
    port: int = 8000


class APiV1Prefix(BaseModel):
    prefix: str = "/v1"
    users: str = "/users"



class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: APiV1Prefix = APiV1Prefix()


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):  # BaseSettings задает основные настройки, ну также может там из файликов брать .env данные
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__"
    )
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig


settings = Settings()
