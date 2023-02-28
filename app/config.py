import os
from functools import lru_cache

from pydantic import BaseSettings
from pydantic import Field
from pydantic import PostgresDsn


class Config(BaseSettings):
    postgres_dsn: PostgresDsn = Field(..., env="POSTGRES_URL")


class DevConfig(Config):
    class Config:
        env_file = ".env.dev"
        env_file_encoding = "utf-8"


class ProdConfig(Config):
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_config() -> Config:
    env = os.getenv("ENV")
    return DevConfig() if env == "dev" else ProdConfig()


config = get_config()
