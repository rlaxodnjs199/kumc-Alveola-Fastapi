import os
from functools import lru_cache
from pydantic import BaseSettings, Field, PostgresDsn


class Config(BaseSettings):
    postgres_dsn: PostgresDsn = Field(..., env="POSTGRES_URL")


class DevConfig(Config):
    class Config:
        env_file = ".env.dev"
        env_file_encoding = "utf-8"


class ProdConfig(Config):
    class Config:
        env_file = ".env.prod"
        env_file_encoding = "utf-8"


@lru_cache
def get_config() -> Config:
    env = os.getenv("ENV")
    if env == "prod":
        return ProdConfig()
    elif env == "dev":
        return DevConfig()


config = get_config()
